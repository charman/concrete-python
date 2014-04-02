#
# Autogenerated by Thrift Compiler (1.0.0-dev)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style,utf8strings
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import concrete.structure.ttypes
import concrete.metadata.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class EntityType(object):
  """
  A span of text with a specific referent, such as a person,
  organization, or time. Things that can be referred to by a mention
  are called "entities."

  It is left up to individual EntityMention taggers to decide which
  referent types and phrase types to identify. For example, some
  EntityMention taggers may only identify proper nouns, or may only
  identify EntityMentions that refer to people.

  Each EntityMention consists of a sequence of tokens. This sequence
  is usually annotated with information about the referent type
  (e.g., is it a person, or a location, or an organization, etc) as
  well as the phrase type (is it a name, pronoun, common noun, etc.).

  EntityMentions typically consist of a single noun phrase; however,
  other phrase types may also be marked as mentions. For
  example, in the phrase "French hotel," the adjective "French" might
  be marked as a mention for France.
  """
  PERSON = 1
  ORGANIZATION = 2
  GPE = 3
  OTHER = 4
  DATE = 5
  FACILITY = 6
  VEHICLE = 7
  WEAPON = 8
  LOCATION = 9
  TIME = 10
  URL = 11
  EMAIL = 12
  MONEY = 13
  PERCENTAGE = 14
  PHONE_NUMBER = 15
  OCCUPATION = 16
  CHEMICAL = 17
  AGE = 18
  PERCENT = 19
  PERSON_NN = 20
  GPE_ITE = 21
  ORGANIZATION_ITE = 22
  JOB_TITLE = 23
  UNKNOWN = 24
  SET = 25
  DURATION = 26

  _VALUES_TO_NAMES = {
    1: "PERSON",
    2: "ORGANIZATION",
    3: "GPE",
    4: "OTHER",
    5: "DATE",
    6: "FACILITY",
    7: "VEHICLE",
    8: "WEAPON",
    9: "LOCATION",
    10: "TIME",
    11: "URL",
    12: "EMAIL",
    13: "MONEY",
    14: "PERCENTAGE",
    15: "PHONE_NUMBER",
    16: "OCCUPATION",
    17: "CHEMICAL",
    18: "AGE",
    19: "PERCENT",
    20: "PERSON_NN",
    21: "GPE_ITE",
    22: "ORGANIZATION_ITE",
    23: "JOB_TITLE",
    24: "UNKNOWN",
    25: "SET",
    26: "DURATION",
  }

  _NAMES_TO_VALUES = {
    "PERSON": 1,
    "ORGANIZATION": 2,
    "GPE": 3,
    "OTHER": 4,
    "DATE": 5,
    "FACILITY": 6,
    "VEHICLE": 7,
    "WEAPON": 8,
    "LOCATION": 9,
    "TIME": 10,
    "URL": 11,
    "EMAIL": 12,
    "MONEY": 13,
    "PERCENTAGE": 14,
    "PHONE_NUMBER": 15,
    "OCCUPATION": 16,
    "CHEMICAL": 17,
    "AGE": 18,
    "PERCENT": 19,
    "PERSON_NN": 20,
    "GPE_ITE": 21,
    "ORGANIZATION_ITE": 22,
    "JOB_TITLE": 23,
    "UNKNOWN": 24,
    "SET": 25,
    "DURATION": 26,
  }

class PhraseType(object):
  """
  Enumeration of phrase types.
  """
  NAME = 1
  PRONOUN = 2
  COMMON_NOUN = 3
  OTHER = 4
  APPOSITIVE = 5
  LIST = 6

  _VALUES_TO_NAMES = {
    1: "NAME",
    2: "PRONOUN",
    3: "COMMON_NOUN",
    4: "OTHER",
    5: "APPOSITIVE",
    6: "LIST",
  }

  _NAMES_TO_VALUES = {
    "NAME": 1,
    "PRONOUN": 2,
    "COMMON_NOUN": 3,
    "OTHER": 4,
    "APPOSITIVE": 5,
    "LIST": 6,
  }


class Entity(object):
  """
  A single referent (or "entity") that is referred to at least once
  in a given communication, along with pointers to all of the
  references to that referent. The referent's type (e.g., is it a
  person, or a location, or an organization, etc) is also recorded.

  Because each Entity contains pointers to all references to a
  referent with a given communication, an Entity can be
  thought of as a coreference set.

  Attributes:
   - uuid: Unique identifier for this entity.
   - mentionIdList: An list of pointers to all of the mentions of this Entity's
  referent.  (type=EntityMention)
   - type: The basic type of this entity's referent.
   - confidence: Confidence score for this individual entity.  You can also set a
  confidence score for an entire EntitySet using the EntitySet's
  metadata.
   - canonicalName: A string containing a representative, canonical, or "best" name
  for this entity's referent.  This string may match one of the
  mentions' text strings, but it is not required to.
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'uuid', None, None, ), # 1
    (2, TType.LIST, 'mentionIdList', (TType.STRING,None), None, ), # 2
    (3, TType.I32, 'type', None, None, ), # 3
    (4, TType.DOUBLE, 'confidence', None, None, ), # 4
    (5, TType.STRING, 'canonicalName', None, None, ), # 5
  )

  def __init__(self, uuid=None, mentionIdList=None, type=None, confidence=None, canonicalName=None,):
    self.uuid = uuid
    self.mentionIdList = mentionIdList
    self.type = type
    self.confidence = confidence
    self.canonicalName = canonicalName

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.uuid = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.mentionIdList = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readString().decode('utf-8')
            self.mentionIdList.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.type = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.DOUBLE:
          self.confidence = iprot.readDouble();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.canonicalName = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Entity')
    if self.uuid is not None:
      oprot.writeFieldBegin('uuid', TType.STRING, 1)
      oprot.writeString(self.uuid.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.mentionIdList is not None:
      oprot.writeFieldBegin('mentionIdList', TType.LIST, 2)
      oprot.writeListBegin(TType.STRING, len(self.mentionIdList))
      for iter6 in self.mentionIdList:
        oprot.writeString(iter6.encode('utf-8'))
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.I32, 3)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    if self.confidence is not None:
      oprot.writeFieldBegin('confidence', TType.DOUBLE, 4)
      oprot.writeDouble(self.confidence)
      oprot.writeFieldEnd()
    if self.canonicalName is not None:
      oprot.writeFieldBegin('canonicalName', TType.STRING, 5)
      oprot.writeString(self.canonicalName.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.uuid is None:
      raise TProtocol.TProtocolException(message='Required field uuid is unset!')
    if self.mentionIdList is None:
      raise TProtocol.TProtocolException(message='Required field mentionIdList is unset!')
    if self.type is None:
      raise TProtocol.TProtocolException(message='Required field type is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class EntitySet(object):
  """
  A theory about the set of entities that are present in a
  message. See also: Entity.

  Attributes:
   - uuid: Unique identifier for this set.
   - metadata: Information about where this set came from.
   - entityList: List of entities in this set.
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'uuid', None, None, ), # 1
    (2, TType.STRUCT, 'metadata', (concrete.metadata.ttypes.AnnotationMetadata, concrete.metadata.ttypes.AnnotationMetadata.thrift_spec), None, ), # 2
    (3, TType.LIST, 'entityList', (TType.STRUCT,(Entity, Entity.thrift_spec)), None, ), # 3
  )

  def __init__(self, uuid=None, metadata=None, entityList=None,):
    self.uuid = uuid
    self.metadata = metadata
    self.entityList = entityList

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.uuid = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.metadata = concrete.metadata.ttypes.AnnotationMetadata()
          self.metadata.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.entityList = []
          (_etype10, _size7) = iprot.readListBegin()
          for _i11 in xrange(_size7):
            _elem12 = Entity()
            _elem12.read(iprot)
            self.entityList.append(_elem12)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('EntitySet')
    if self.uuid is not None:
      oprot.writeFieldBegin('uuid', TType.STRING, 1)
      oprot.writeString(self.uuid.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.metadata is not None:
      oprot.writeFieldBegin('metadata', TType.STRUCT, 2)
      self.metadata.write(oprot)
      oprot.writeFieldEnd()
    if self.entityList is not None:
      oprot.writeFieldBegin('entityList', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.entityList))
      for iter13 in self.entityList:
        iter13.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.uuid is None:
      raise TProtocol.TProtocolException(message='Required field uuid is unset!')
    if self.entityList is None:
      raise TProtocol.TProtocolException(message='Required field entityList is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class EntityMention(object):
  """
  A span of text with a specific referent, such as a person,
  organization, or time. Things that can be referred to by a mention
  are called "entities."

  It is left up to individual EntityMention taggers to decide which
  referent types and phrase types to identify. For example, some
  EntityMention taggers may only identify proper nouns, or may only
  identify EntityMentions that refer to people.

  Each EntityMention consists of a sequence of tokens. This sequence
  is usually annotated with information about the referent type
  (e.g., is it a person, or a location, or an organization, etc) as
  well as the phrase type (is it a name, pronoun, common noun, etc.).

  EntityMentions typically consist of a single noun phrase; however,
  other phrase types may also be marked as mentions. For
  example, in the phrase "French hotel," the adjective "French" might
  be marked as a mention for France.

  Attributes:
   - uuid
   - tokens: List of mentions in this set.
   - entityType: The type of referent that is referred to by this mention.
   - phraseType: The phrase type of the tokens that constitute this mention.
   - confidence: A confidence score for this individual mention.  You can also
  set a confidence score for an entire EntityMentionSet using the
  EntityMentionSet's metadata.
   - text: The text content of this entity mention.  This field is
  typically redundant with the 'token_sequence' field, and may not
  be generated by all analytics.
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'uuid', None, None, ), # 1
    (2, TType.STRUCT, 'tokens', (concrete.structure.ttypes.TokenRefSequence, concrete.structure.ttypes.TokenRefSequence.thrift_spec), None, ), # 2
    (3, TType.I32, 'entityType', None, None, ), # 3
    (4, TType.I32, 'phraseType', None, None, ), # 4
    (5, TType.DOUBLE, 'confidence', None, None, ), # 5
    (6, TType.STRING, 'text', None, None, ), # 6
  )

  def __init__(self, uuid=None, tokens=None, entityType=None, phraseType=None, confidence=None, text=None,):
    self.uuid = uuid
    self.tokens = tokens
    self.entityType = entityType
    self.phraseType = phraseType
    self.confidence = confidence
    self.text = text

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.uuid = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.tokens = concrete.structure.ttypes.TokenRefSequence()
          self.tokens.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.entityType = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.phraseType = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.DOUBLE:
          self.confidence = iprot.readDouble();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.text = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('EntityMention')
    if self.uuid is not None:
      oprot.writeFieldBegin('uuid', TType.STRING, 1)
      oprot.writeString(self.uuid.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.tokens is not None:
      oprot.writeFieldBegin('tokens', TType.STRUCT, 2)
      self.tokens.write(oprot)
      oprot.writeFieldEnd()
    if self.entityType is not None:
      oprot.writeFieldBegin('entityType', TType.I32, 3)
      oprot.writeI32(self.entityType)
      oprot.writeFieldEnd()
    if self.phraseType is not None:
      oprot.writeFieldBegin('phraseType', TType.I32, 4)
      oprot.writeI32(self.phraseType)
      oprot.writeFieldEnd()
    if self.confidence is not None:
      oprot.writeFieldBegin('confidence', TType.DOUBLE, 5)
      oprot.writeDouble(self.confidence)
      oprot.writeFieldEnd()
    if self.text is not None:
      oprot.writeFieldBegin('text', TType.STRING, 6)
      oprot.writeString(self.text.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.uuid is None:
      raise TProtocol.TProtocolException(message='Required field uuid is unset!')
    if self.tokens is None:
      raise TProtocol.TProtocolException(message='Required field tokens is unset!')
    if self.entityType is None:
      raise TProtocol.TProtocolException(message='Required field entityType is unset!')
    if self.phraseType is None:
      raise TProtocol.TProtocolException(message='Required field phraseType is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class EntityMentionSet(object):
  """
  A theory about the set of entity mentions that are present in a
  message. See also: EntityMention

  This type does not represent a coreference relationship, which is handled by Entity.
  This type is meant to represent the output of a entity-mention-identifier,
  which is often a part of an in-doc coreference system.

  Attributes:
   - uuid: Unique identifier for this set.
   - metadata: Information about where this set came from.
   - mentionSet: List of mentions in this set.
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'uuid', None, None, ), # 1
    (2, TType.STRUCT, 'metadata', (concrete.metadata.ttypes.AnnotationMetadata, concrete.metadata.ttypes.AnnotationMetadata.thrift_spec), None, ), # 2
    (3, TType.LIST, 'mentionSet', (TType.STRUCT,(EntityMention, EntityMention.thrift_spec)), None, ), # 3
  )

  def __init__(self, uuid=None, metadata=None, mentionSet=None,):
    self.uuid = uuid
    self.metadata = metadata
    self.mentionSet = mentionSet

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.uuid = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.metadata = concrete.metadata.ttypes.AnnotationMetadata()
          self.metadata.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.mentionSet = []
          (_etype17, _size14) = iprot.readListBegin()
          for _i18 in xrange(_size14):
            _elem19 = EntityMention()
            _elem19.read(iprot)
            self.mentionSet.append(_elem19)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('EntityMentionSet')
    if self.uuid is not None:
      oprot.writeFieldBegin('uuid', TType.STRING, 1)
      oprot.writeString(self.uuid.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.metadata is not None:
      oprot.writeFieldBegin('metadata', TType.STRUCT, 2)
      self.metadata.write(oprot)
      oprot.writeFieldEnd()
    if self.mentionSet is not None:
      oprot.writeFieldBegin('mentionSet', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.mentionSet))
      for iter20 in self.mentionSet:
        iter20.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.uuid is None:
      raise TProtocol.TProtocolException(message='Required field uuid is unset!')
    if self.mentionSet is None:
      raise TProtocol.TProtocolException(message='Required field mentionSet is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
