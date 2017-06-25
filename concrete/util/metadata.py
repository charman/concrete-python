from __future__ import unicode_literals
from datetime import datetime
import json


EPOCH = datetime.utcfromtimestamp(0)


class ZeroAnnotationsError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class MultipleAnnotationsError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


def datetime_to_timestamp(dt):
    '''
    Given time-zone--unaware datetime object representing date and time
    in UTC, return corresponding Concrete timestamp.

    Args:
        dt(datetime): time-zone--unaware datetime object representing
        date and time (in UTC) to convert

    Source:
    http://stackoverflow.com/questions/6999726/how-can-i-convert-a-datetime-object-to-milliseconds-since-epoch-unix-time-in-p
    '''
    return int((dt - EPOCH).total_seconds())


def timestamp_to_datetime(timestamp):
    '''
    Given Concrete timestamp, return corresponding time-zone--unaware
    datetime object representing date and time in UTC.

    Args:
        timestamp(int): Concrete timestamp (integer representing
            seconds since the epoch in UTC) representing date and time
            to convert

    Source:
    https://stackoverflow.com/questions/3694487/initialize-a-datetime-object-with-seconds-since-epoch
    '''
    return datetime.utcfromtimestamp(timestamp)


def now_timestamp():
    '''
    Return timestamp representing the current time.
    '''
    return datetime_to_timestamp(datetime.now())


def get_index_of_tool(lst_of_conc, tool):
    """Return the index of the object in the provided list
    whose tool name matches tool.

    If tool is None, return the first valid index into `lst_of_conc`.

    This returns -1 if:
      * `lst_of_conc` is None, or
      * `lst_of_conc` has no entries, or
      * no object in `lst_of_conc` matches `tool`.

    Args:

    - `lst_of_conc`: A list of Concrete objects, each of which
      has a `.metadata` field.
    - `tool`: A tool name to match.
    """
    idx = -1
    if lst_of_conc is not None and len(lst_of_conc) > 0:
        if tool is not None:
            for (cidx, obj) in enumerate(lst_of_conc):
                if obj.metadata.tool == tool:
                    idx = cidx
                    break
        else:
            idx = 0
    return idx


def get_annotation_field(annotation, field):
    '''
    Return requested field of annotation metadata.

    Args:
        annotation: object containing a `metadata` field of
            type :class:`..metadata.ttypes.AnnotationMetadata`.
        field: name of metadata field: kBest, timestamp, or tool.

    Returns:
        value of requested field in annotation metadata.
    '''
    if field == 'kBest':
        return annotation.metadata.kBest
    elif field == 'timestamp':
        return annotation.metadata.timestamp
    elif field == 'tool':
        return annotation.metadata.tool
    else:
        raise ValueError('unrecognized field {}'.format(field))


def filter_annotations(annotations,
                       sort_field=None,
                       sort_reverse=False,
                       action_if_multiple='pass',
                       action_if_zero='pass',
                       **filter_field_value_pairs):
    '''
    Return filtered and/or re-ordered list of annotations, that is,
    objects containing a `metadata` field of type AnnotationMetadata.

    Args:
        annotations (list): original list of annotations (objects
            containing a `metadata` field of type
            :class:`..metadata.ttypes.AnnotationMetadata`).
            This list is not modified.
        sort_field (str): field by which to re-order annotations.
            Default: do not re-order annotations.
        sort_reverse (bool): True to reverse order of annotations
            (after sorting, if any).
        action_if_multiple (str): action to take if, after filtering,
            there is more than one annotation left.  'pass' to
            return all filtered and re-ordered annotations, 'raise' to
            raise an exception of type `MultipleAnnotationsError`,
            'first' to return a list containing the first annotation
            after filtering and re-ordering, or 'last' to return a list
            containing the last annotation after filtering and
            re-ordering.
        action_if_zero (str): action to take if, after filtering, there
            are no annotations left.  'pass' to return an empty list,
            'raise to raise an exception of type `ZeroAnnotationsError`.
        filter_field_value_pairs: field-value pairs (for example:
            `tool='goldenhorse', kBest=1`) by which to filter
            annotations (keep annotations whose field `FIELD` not equals
            `VALUE` for all (`FIELD`, `VALUE`) pairs).  Default: keep
            all annotations.  See :func:`get_annotation_field` for valid
            fields.

    Returns:
        filtered and/or re-ordered list of annotations
    '''
    annotations = list(annotations)

    if filter_field_value_pairs:
        annotations = [
            a for a in annotations
            if all(
                get_annotation_field(a, field) == value
                for (field, value) in filter_field_value_pairs.items()
            )
        ]

    if sort_field:
        annotations = sorted(
            annotations,
            key=lambda a: get_annotation_field(a, sort_field))

    if sort_reverse:
        annotations = annotations[::-1]

    if len(annotations) == 0:
        if action_if_zero == 'raise':
            raise ZeroAnnotationsError()
        elif action_if_zero == 'pass':
            pass
        else:
            raise ValueError('unknown action_if_zero value {}'.format(
                action_if_zero))
    elif len(annotations) > 1:
        if action_if_multiple == 'raise':
            raise MultipleAnnotationsError()
        elif action_if_multiple == 'pass':
            pass
        elif action_if_multiple == 'first':
            annotations = [annotations[0]]
        elif action_if_multiple == 'last':
            annotations = [annotations[-1]]
        else:
            raise ValueError('unknown action_if_multiple value {}'.format(
                action_if_multiple))

    return annotations


def filter_annotations_json(annotations, kwargs_json):
    '''
    Call :func:`filter_annotations` on `annotations`, sending it
    keyword arguments from the JSON-encoded dictionary
    `kwargs_json`.

    Args:
        annotations (list): original list of annotations (objects
            containing a `metadata` field of type
            :class:`..metadata.ttypes.AnnotationMetadata`).
            This list is not modified.
        kwargs_json (str): JSON-encoded dictionary of keyword
            arguments to be passed to :func:`filter_annotations`.

    Returns:
        `annotations` filtered by :func:`filter_annotations` according
        to provided JSON-encoded keyword arguments.
    '''

    return filter_annotations(annotations, **json.loads(kwargs_json))
