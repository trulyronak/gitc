#!/usr/bin/python

import os
import sys

args = sys.argv
commitMsg = "quick commit"
if len(sys.argv) == 1:
    print "Pushing, Commit Message is 'quick commit'"
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
