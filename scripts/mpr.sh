#!/usr/bin/env bash

#TODO there is an argument to be made for keeping this script in the root of the directory (so that the invocation command is just ./mpr, not ./scripts/mpr

USERNAME=whoami
echo "Creating a pull request for user" $USERNAME

git push
