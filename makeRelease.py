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

    feedback = validateOptions(options)

    if 0 == feedback:
        repo = git.Repo('.')
        print(str(repo.git.status()))
    else:
        parser.print_help()

    return feedback


#---------------------------------------------------------------------------
# Check if all options are set and valid
def validateOptions(options):
    feedback = 0
    if not options.source:
        feedback = 1
    if not options.destination:
        feedback = 2
    if not options.releaseVersion:
        feedback = 3
    if not options.nextVersion:
        feedback = 4
    return feedback

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
