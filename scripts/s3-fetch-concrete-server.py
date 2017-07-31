#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging

from boto import connect_s3
import concrete.version
from concrete.util import (
    set_stdout_encoding,
    S3BackedCommunicationContainer,
    CommunicationContainerFetchHandler,
    FetchCommunicationServiceWrapper,
    DEFAULT_S3_KEY_PREFIX_LEN,
)


def main():
    set_stdout_encoding()

    parser = argparse.ArgumentParser(
        description='Run a fetch server backed by an AWS S3 bucket '
                    '(keyed by communication id).',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument('bucket_name', help='name of S3 bucket to read from')
    parser.add_argument('--host', help='hostname to serve on',
                        default='localhost')
    parser.add_argument('--port', type=int, help='port to serve on',
                        default=9090)
    parser.add_argument('--prefix-len', type=int, default=DEFAULT_S3_KEY_PREFIX_LEN,
                        help='S3 keys are prefixed with hashes of this length')
    parser.add_argument('-l', '--loglevel',
                        help='Logging verbosity level threshold (to stderr)',
                        default='info')
    concrete.version.add_argparse_argument(parser)
    args = parser.parse_args()

    logging.basicConfig(format='%(levelname)7s:  %(message)s', level=args.loglevel.upper())

    logging.info('connecting to s3')
    conn = connect_s3()
    logging.info('retrieving bucket {}'.format(args.bucket_name))
    bucket = conn.get_bucket(args.bucket_name)
    logging.info('reading from s3 bucket {}, prefix length {}'.format(
        args.bucket_name, args.prefix_len))
    container = S3BackedCommunicationContainer(bucket, args.prefix_len)
    handler = CommunicationContainerFetchHandler(container)
    logging.info('hosting fetch service at {}:{}'.format(args.host, args.port))
    server = FetchCommunicationServiceWrapper(handler)
    server.serve(args.host, args.port)


if __name__ == "__main__":
    main()
