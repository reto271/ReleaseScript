#!/usr/bin/env python3
# encoding: utf-8

import unittest
import os
import makeRelease

class Test_MakeRelease(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_testValidReleaseVersion(self):
        testDate = makeRelease.validateNextVersion('V12.34 B01')
        self.assertEqual(True, testDate)

    def test_testValidReleaseVersion_wrongV(self):
        testDate = makeRelease.validateNextVersion('v12.34 B12')
        self.assertEqual(False, testDate)

    def test_testValidReleaseVersion_wrongSeparator(self):
        testDate = makeRelease.validateNextVersion('V12,34 B89')
        self.assertEqual(False, testDate)

    def test_testValidReleaseVersion_wrongMajor(self):
        testDate = makeRelease.validateNextVersion('V1a.34 B12')
        self.assertEqual(False, testDate)

    def test_testValidReleaseVersion_wrongMinor(self):
        testDate = makeRelease.validateNextVersion('V12.3f B55')
        self.assertEqual(False, testDate)

    def test_testValidReleaseVersion_majorToShort(self):
        testDate = makeRelease.validateNextVersion('V1.30 B00')
        self.assertEqual(False, testDate)

    def test_testValidReleaseVersion_minorToShort(self):
        testDate = makeRelease.validateNextVersion('V88.3 B10')
        self.assertEqual(False, testDate)

    def test_testValidReleaseVersion_(self):
        testDate = makeRelease.validateNextVersion('V88.33B10')
        self.assertEqual(False, testDate)

    def test_testValidReleaseVersion_(self):
        testDate = makeRelease.validateNextVersion('V88.33 b10')
        self.assertEqual(False, testDate)

    def test_testValidReleaseVersion_(self):
        testDate = makeRelease.validateNextVersion('V88.33_B10')
        self.assertEqual(False, testDate)

    def test_testValidReleaseVersion_(self):
        testDate = makeRelease.validateNextVersion('V88.33-B10')
        self.assertEqual(False, testDate)

    def test_testValidReleaseVersion_(self):
        testDate = makeRelease.validateNextVersion('V88.33 B1a')
        self.assertEqual(False, testDate)

    def test_testValidReleaseVersion_(self):
        testDate = makeRelease.validateNextVersion('V88.33 B10')
        self.assertEqual(False, testDate)

    def test_testValidReleaseVersion_(self):
        testDate = makeRelease.validateNextVersion('V88.33 B1')
        self.assertEqual(False, testDate)


if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
    #unittest.main()  # Calling from the command line invokes all tests
