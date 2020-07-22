#!/usr/bin/env bash

# Remove the git tracking
rm -rf ${PWD}/.git* || rm -rf ${PWD}/Ricevute/.git*

# Get the repository -> "Ricevute" directory
git clone https://github.com/mircomannino/Ricevute.git

# Get file from directory and delete it
rm -r __pychache__
mv ${PWD}/Ricevute/* ./
rm -rf Ricevute
