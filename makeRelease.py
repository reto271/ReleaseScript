#!/usr/bin/env python3
# encoding: utf-8

import git
import argparse
import os.path
import os
from datetime import date


#---------------------------------------------------------------------------
def main():
    """ The main entry point of the analyse log script
    """
    parser = parseCmdLine()
    options = parser.parse_args()

    repo = git.Repo('.')
    feedback = validateOptions(repo, options)

    if 0 == feedback:
        #print(str(repo.git.status()))
        pass
    else:
        parser.print_help()

    return feedback


#---------------------------------------------------------------------------
# Check if all options are set and valid
def validateOptions(repo, options):
    feedback = 0
    if not options.source:
        feedback = 1
    if not options.destination:
        feedback = 2
    if not options.releaseVersion:
        feedback = 3
    if not options.nextVersion:
        feedback = 4

    if 0 == feedback:
        feedback = checkIfBranchExists(repo, options.source)
    if 0 == feedback:
        feedback = checkIfBranchExists(repo, options.destination)
    if 0 == feedback:
        feedback = validateReleaseVersion(options.releaseVersion)
    if 0 == feedback:
        feedback = validateNextVersion(options.source)
    return feedback

def checkIfBranchExists(repo, branchName):
    feedback = 5
    for br in repo.branches:
        if str(br) == str(branchName):
            feedback = 0
    if 0 != feedback:
        print('Branch: "' + branchName + '" does not exist in git repo.')
    return feedback

def validateReleaseVersion(releaseVersion):
    feedback = 0
    leadingV = releaseVersion[0:1]
    majorV = tryInt(releaseVersion[1:3])
    minorV = tryInt(releaseVersion[4:6])
    separater = releaseVersion[3:4]

    if 'V' != leadingV:
        feedback = 6
    if ((0 > majorV) or (99 < majorV)):
        feedback = 7
    if ((0 > minorV) or (99 < minorV)):
        feedback = 8
    if '.' != separater:
        feedback = 9
    return feedback

def validateNextVersion(nextVersion):
    feedback = 0
    return feedback

# Try if it is an int and return a default value
def tryInt(s, val=-1):
  try:
    return int(s)
  except ValueError:
    return val

#---------------------------------------------------------------------------
def parseCmdLine():
    ''' Parse the command line. '''
    parser = argparse.ArgumentParser(description="Door Bot Log File Analyzer")
    parser.add_argument('-s', '--source', default=None, help='Source branch name')
    parser.add_argument('-d', '--destination', default=None, help='Destination branch name')
    parser.add_argument('-r', '--releaseVersion', default=None, help='Version of the release')
    parser.add_argument('-n', '--nextVersion', default=None, help='Next version on the source branch')
    return parser



#---------------------------------------------------------------------------
if __name__ == '__main__':
    exit(main())
