#!/usr/bin/env python3
# encoding: utf-8

import git
import argparse
import os.path
import os
import subprocess

#---------------------------------------------------------------------------
def main():
    """ The main entry point of the release log script.
        ./makeRelease.sh  --source=develop --destination=main --releaseVersion=V00.21 --nextVersion="V00.22 B01"
        creates a release on with V0.21 on the main brnach. It merges the changes
        from develop. The version on the develop will be V00.22 B01 after the script
        finished.
    """

    printVersionNumber()

    parser = parseCmdLine()
    options = parser.parse_args()

    repo = git.Repo('.')
    feedback = validateOptions(repo, options)

    if True == feedback:
        makeRelease(repo, options)
        return 0
    else:
        parser.print_help()
        return 1



#---------------------------------------------------------------------------
# Check if all options are set and valid
def makeRelease(repo, options):
    # checkout the branch using git-checkout. It will fail as the working tree appears dirty
    print(str(repo.heads))

    # Test if the release branch is available
    try:
        repo.git.checkout(options.destination)
    except:
        print('Could not checkout branch "' + options.destination + '". There are might be local changes in the current branch.')
        return False

    # Test if the target branch is available and prepare the release
    try:
        repo.git.checkout(options.source)
    except:
        print('Could not checkout branch "' + options.source + '". There are might be local changes in the current branch.')
        return False

    setVersionNumberAndCommit(repo, options.releaseVersion)

    try:
        repo.git.checkout(options.destination)
    except:
        print('Could not checkout branch "' + options.destination + '". There are might be local changes in the current branch.')
        return False

    # Merge the branch
    feedback = runMerge(options.source, options.releaseVersion)

    if True == feedback:
        repo.remotes.origin.push()
        try:
            repo.git.checkout(options.source)
        except:
            print('Could not checkout branch "' + options.source + '". There are might be local changes in the current branch.')
            return False

        setVersionNumberAndCommit(repo, options.nextVersion)
        repo.remotes.origin.push()

    return True

#---------------------------------------------------------------------------
# Set the version number on the current branch
def setVersionNumberAndCommit(repo, verNumber):
    setVersionNumber(verNumber)
    repo.index.add('VersionNumber.txt')
    repo.git.commit('-m', 'Set version number to ' + verNumber)

#---------------------------------------------------------------------------
# Merge the branch
def runMerge(sourceBranch, versionNr):
    print('runMerge')
    #cmd = ['git', '-C', path, 'branch', '-a']
    cmd = ['git', 'merge', '--no-ff', '-m ' + versionNr,  sourceBranch ]
    print(cmd)
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        return True
    except:
        print('Could not merge')
        return False


#---------------------------------------------------------------------------
# Write the version number to the version file
def setVersionNumber(versionNumber):
    with open('VersionNumber.txt', 'w') as f:
        f.write(versionNumber + '\n')
        f.close()


#---------------------------------------------------------------------------
# Check if all options are set and valid
def validateOptions(repo, options):
    feedback = True
    if not options.source:
        feedback = False
    if not options.destination:
        feedback = False
    if not options.releaseVersion:
        feedback = False
    if not options.nextVersion:
        feedback = False

    if True == feedback:
        feedback = checkIfBranchExists(repo, options.source)
    if True == feedback:
        feedback = checkIfBranchExists(repo, options.destination)
    if True == feedback:
        feedback = validateReleaseVersion(options.releaseVersion)
    if True == feedback:
        feedback = validateNextVersion(options.nextVersion)
    return feedback


#---------------------------------------------------------------------------
# Checks if a given branch exists
def checkIfBranchExists(repo, branchName):
    feedback = False
    for br in repo.branches:
        if str(br) == str(branchName):
            feedback = True
    if False == feedback:
        print('Branch: "' + branchName + '" does not exist in git repo.')
    return feedback


#---------------------------------------------------------------------------
# Validates the release version
def validateReleaseVersion(releaseVersion):
    feedback = True
    leadingV = releaseVersion[0:1]
    majorV = tryInt(releaseVersion[1:3])
    minorV = tryInt(releaseVersion[4:6])
    separater = releaseVersion[3:4]
    strLen = len(releaseVersion)

    if 'V' != leadingV:
        feedback = False
    if ((0 > majorV) or (99 < majorV)):
        feedback = False
    if ((0 > minorV) or (99 < minorV)):
        feedback = False
    if '.' != separater:
        feedback = False
    if 6 != strLen:
        feedback = False
    return feedback


#---------------------------------------------------------------------------
# Validate the next version
def validateNextVersion(nextVersion):
    feedback = True
    leadingV = nextVersion[0:1]
    majorV = tryInt(nextVersion[1:3])
    minorV = tryInt(nextVersion[4:6])
    separator1 = nextVersion[3:4]
    separator2 = nextVersion[6:8]
    betaV = tryInt(nextVersion[8:10])
    strLen = len(nextVersion)

    if 'V' != leadingV:
        feedback = False
    if ((0 > majorV) or (99 < majorV)):
        feedback = False
    if ((0 > minorV) or (99 < minorV)):
        feedback = False
    if ((0 > betaV) or (99 < betaV)):
        feedback = False
    if '.' != separator1:
        feedback = False
    if 10 != strLen:
        feedback = False
    return feedback


#---------------------------------------------------------------------------
# Try if it is an int and return a default value
def tryInt(s, val=-1):
  try:
    return int(s)
  except ValueError:
    return val


#---------------------------------------------------------------------------
# Defines the commands
def parseCmdLine():
    ''' Parse the command line. '''
    parser = argparse.ArgumentParser(description="Door Bot Log File Analyzer")
    parser.add_argument('-s', '--source', default=None, help='Source branch name')
    parser.add_argument('-d', '--destination', default=None, help='Destination branch name')
    parser.add_argument('-r', '--releaseVersion', default=None, help='Version of the release')
    parser.add_argument('-n', '--nextVersion', default=None, help='Next version on the source branch')
    return parser

#---------------------------------------------------------------------------
# Prints the version number
def printVersionNumber():
    try:
        with open('VersionNumber.txt', 'r') as versionFile:
            versionNumber = versionFile.read().rstrip()
            print('Version: ' + str(versionNumber))
            versionFile.close()
    except:
        print('File ' + str(logFileName) + ' not found.')
        return -2



#---------------------------------------------------------------------------
if __name__ == '__main__':
    exit(main())
