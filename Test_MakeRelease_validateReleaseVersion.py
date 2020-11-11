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
        testDate = makeRelease.validateReleaseVersion('V12.34')
        self.assertEqual(True, testDate)

    def test_testValidReleaseVersion_wrongV(self):
        testDate = makeRelease.validateReleaseVersion('v12.34')
        self.assertEqual(False, testDate)

    def test_testValidReleaseVersion_wrongSeparator(self):
        testDate = makeRelease.validateReleaseVersion('V12,34')
        self.assertEqual(False, testDate)

    def test_testValidReleaseVersion_wrongMajor(self):
        testDate = makeRelease.validateReleaseVersion('V1a.34')
        self.assertEqual(False, testDate)

    def test_testValidReleaseVersion_wrongMinor(self):
        testDate = makeRelease.validateReleaseVersion('V12.3f')
        self.assertEqual(False, testDate)

    def test_testValidReleaseVersion_majorToShort(self):
        testDate = makeRelease.validateReleaseVersion('V1.30')
        self.assertEqual(False, testDate)

    def test_testValidReleaseVersion_minorToShort(self):
        testDate = makeRelease.validateReleaseVersion('V88.3')
        self.assertEqual(False, testDate)

if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
    #unittest.main()  # Calling from the command line invokes all tests
