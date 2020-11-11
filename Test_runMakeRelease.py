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
        self.assertEqual(0, testDate)

    def test_testValidReleaseVersion_wrongV(self):
        testDate = makeRelease.validateReleaseVersion('v12.34')
        self.assertEqual(6, testDate)

    def test_testValidReleaseVersion_wrongSeparator(self):
        testDate = makeRelease.validateReleaseVersion('V12,34')
        self.assertEqual(9, testDate)

    def test_testValidReleaseVersion_wrongMajor(self):
        testDate = makeRelease.validateReleaseVersion('V1a.34')
        self.assertEqual(7, testDate)

    def test_testValidReleaseVersion_wrongMinor(self):
        testDate = makeRelease.validateReleaseVersion('V12,3f')
        self.assertEqual(9, testDate)

if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
    #unittest.main()  # Calling from the command line invokes all tests
