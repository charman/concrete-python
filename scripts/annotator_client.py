from thrift import Thrift, TSerialization
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from thrift.server import TServer

from concrete.services import *
from concrete.services.ttypes import *

from concrete.communication import *
from concrete.communication.ttypes import *

import argparse
import codecs
import sys, os

from concrete.util.annotator_wrapper import AnnotatorClientWrapper
from concrete.util import (read_communication_from_file, CommunicationWriter)

def main():
    # Make stdout output UTF-8, preventing "'ascii' codec can't encode" errors
    sys.stdout = codecs.getwriter('utf8')(sys.stdout)

    parser = argparse.ArgumentParser(description="Interface with a Concrete Annotator service")
    parser.add_argument('--port', required=True, default=33221, type=int, help="Port to use. [Default: 33221]")
    parser.add_argument('--host', required=True, help="Hostname to use.")
    parser.add_argument('--input', required=True, default='-', help="Input source to use. '-' for stdin; otherwise takes a path to a file. [Default: stdin]")
    parser.add_argument('--output', required=True, default='-', help="Output source to use. '-' for stdout; otherwise takes a path to a file. [Default: stdout]")
    args = parser.parse_args()

    if args.input == '-':
        # ???
        handle = os.fdopen(sys.stdin.fileno(), 'rb')
        try:
            bytez = handle.read()
            comm = Communication()
            TSerialization.deserialize(comm, bytez, protocol_factory=TCompactProtocol.TCompactProtocolFactory())
        finally:
            handle.close()
    else:
        comm = read_communication_from_file(args.input)

    cli = AnnotatorClientWrapper(args.host, args.port)
    new_comm = cli.annotate(comm)

    if args.output == '-':
        new_bytes = TSerialization.serialize(new_comm, protocol_factory=TCompactProtocol.TCompactProtocolFactory())
        handle = os.fdopen(sys.stdout.fileno(), 'wb')
        try:
            handle.write(new_bytes)
        finally:
            handle.close()

    else:
        wrtr = CommunicationWriter(args.output)
        wrtr.write(new_comm)
        wrtr.close()

if __name__ == "__main__":
    main()