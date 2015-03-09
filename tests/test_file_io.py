#!/usr/bin/env python

"""
"""

import os
import tarfile
import tempfile
import unittest

from concrete.util import (
    CommunicationReader,
    CommunicationWriter,
    CommunicationWriterTGZ,
    read_communication_from_file
)
from concrete.validate import validate_communication

class TestCommunicationReader(unittest.TestCase):
    def test_single_file(self):
        filename = u'tests/testdata/simple_1.concrete'
        reader = CommunicationReader(filename)
        comm1 = reader.next()
        self.assertEqual(u'one', comm1.id)
        self.assertEqual(filename, comm1.filename)

    def test_single_gz_file(self):
        filename = u'tests/testdata/simple_1.concrete.gz'
        reader = CommunicationReader(filename)
        comm1 = reader.next()
        self.assertEqual(u'one', comm1.id)
        self.assertEqual(filename, comm1.filename)

    def test_concatenated_file(self):
        filename = u'tests/testdata/simple_concatenated'
        reader = CommunicationReader(filename)
        comms = [c for c in reader]
        for (i, comm_id) in enumerate([u'one', u'two', u'three']):
            self.assertEqual(comm_id, comms[i].id)
            self.assertEqual(filename, comms[i].filename)

    def test_concatenated_gz_file(self):
        filename = u'tests/testdata/simple_concatenated.gz'
        reader = CommunicationReader(filename)
        comms = [c for c in reader]
        for (i, comm_id) in enumerate([u'one', u'two', u'three']):
            self.assertEqual(comm_id, comms[i].id)
            self.assertEqual(filename, comms[i].filename)

    def test_tar_file(self):
        filename = u'tests/testdata/simple.tar'
        reader = CommunicationReader(filename)
        comms = [c for c in reader]
        self.assertEqual(u'one', comms[0].id)
        self.assertEqual(u'two', comms[1].id)
        self.assertEqual(u'three', comms[2].id)
        self.assertEqual(u'simple_1.concrete', comms[0].filename)
        self.assertEqual(u'simple_2.concrete', comms[1].filename)
        self.assertEqual(u'simple_3.concrete', comms[2].filename)

    def test_tar_gz_file(self):
        reader = CommunicationReader("tests/testdata/simple.tar.gz")
        comms = [c for c in reader]
        self.assertEqual(u'one', comms[0].id)
        self.assertEqual(u'two', comms[1].id)
        self.assertEqual(u'three', comms[2].id)
        self.assertEqual(u'simple_1.concrete', comms[0].filename)
        self.assertEqual(u'simple_2.concrete', comms[1].filename)
        self.assertEqual(u'simple_3.concrete', comms[2].filename)

    def test_zip_file(self):
        reader = CommunicationReader("tests/testdata/simple.zip")
        comms = [c for c in reader]
        self.assertEqual(u'one', comms[0].id)
        self.assertEqual(u'two', comms[1].id)
        self.assertEqual(u'three', comms[2].id)
        self.assertEqual(u'simple_1.concrete', comms[0].filename)
        self.assertEqual(u'simple_2.concrete', comms[1].filename)
        self.assertEqual(u'simple_3.concrete', comms[2].filename)


class TestCommunicationWriter(unittest.TestCase):
    def test_single_file(self):
        comm = read_communication_from_file("tests/testdata/simple_1.concrete")
        writer = CommunicationWriter()
        (file_handle, filename) = tempfile.mkstemp()
        writer.open(filename)
        writer.write(comm)
        writer.close()

        os.remove(filename)


class TestCommunicationWriterTGZ(unittest.TestCase):
    def test_single_file(self):
        comm = read_communication_from_file("tests/testdata/simple_1.concrete")
        writer = CommunicationWriterTGZ()
        (file_handle, filename) = tempfile.mkstemp()
        writer.open(filename)
        writer.write(comm, "simple_1.concrete")
        writer.close()

        self.assertTrue(tarfile.is_tarfile(filename))
        os.remove(filename)


if __name__ == '__main__':
    unittest.main(buffer=True)