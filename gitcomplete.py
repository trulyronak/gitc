#!/usr/bin/python

import os
import sys

DEFAULT_COMMIT_MSG = "quick commit"
args = sys.argv
commitMsg = DEFAULT_COMMIT_MSG
if len(sys.argv) == 1:
    print "Pushing, Commit Message is " + DEFAULT_COMMIT_MSG
else:
    del args[0]
    commitMsg = ' '.join(args)
commitCmd = 'git commit -m "' + commitMsg +'"'
os.system('git add -A')
os.system(commitCmd)
print ''

os.system('git status')
print ''
print 'Thank you for using GitC'
