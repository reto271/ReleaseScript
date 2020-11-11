#!/usr/bin/env python3
# encoding: utf-8

import unittest
import os
import makeRelease

class Mock_repo:
    def __init__(self):
        self.branches = []
        self.branches.append('main')
        self.branches.append('develop')


class Test_MakeRelease(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

    def setUp(self):
        self.myRepo = Mock_repo()

    def tearDown(self):
        pass

    def test_testBranchExisting_main(self):
        testDate = makeRelease.checkIfBranchExists(self.myRepo, 'main')
        self.assertEqual(True, testDate)

    def test_testBranchExisting_develop(self):
        testDate = makeRelease.checkIfBranchExists(self.myRepo, 'develop')
        self.assertEqual(True, testDate)

    def test_testBranchNotExisting_master(self):
        testDate = makeRelease.checkIfBranchExists(self.myRepo, 'master')
        self.assertEqual(False, testDate)

if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
    #unittest.main()  # Calling from the command line invokes all tests
