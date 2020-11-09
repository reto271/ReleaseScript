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
    feedback = 1
    options = parse_options()

    # Check if all options are set and valid
    if not options.source:
        feedback = 2
    if not options.destination:
        feedback = 3
    if not options.releaseVersion:
        feedback = 4
    if not options.nextVersion:
        feedback = 5
    feedback = 0

    repo = git.Repo('.')
    print(str(repo.git.status()))

    return feedback


#---------------------------------------------------------------------------
def parse_options():
    ''' Parse the command line. '''
    parser = argparse.ArgumentParser(description="Door Bot Log File Analyzer")
    parser.add_argument('-s', '--source', default=None, help='Source branch name')
    parser.add_argument('-d', '--destination', default=None, help='Destination branch name')
    parser.add_argument('-r', '--releaseVersion', default=None, help='Version of the release')
    parser.add_argument('-n', '--nextVersion', default=None, help='Next version on the source branch')
    options = parser.parse_args()
    return options



#---------------------------------------------------------------------------
if __name__ == '__main__':
    exit(main())
