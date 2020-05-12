#!/bin/bash

set -e
if [ $# -eq 0 ]; then
	git add -A
    git commit -m "Pushing Quick Commit";
else
	if [ '${*,,}' = "bug fix" ]; then
	  echo "Please, you can do better than this"
	  exit 1
	else
		if [ '${*,,}' = "validation bug fix" ]; then 
			echo "I could do this all day, do better"
			exit 1
		else
			git add -A
			git commit -m "$*";
		fi
	fi
fi
git push;
# if [[ $* = *"bug fix"* ]]; then
# 	  echo "It's there!"
# 	fi
    