#!/usr/bin/env bash

# Remove the git tracking
rm -rf ${PWD}/.git* || rm -rf ${PWD}/.git*


# Get the repository -> "Ricevute" directory
git clone https://github.com/mircomannino/Ricevute.git

# Get file from directory and delete it
mv ${PWD}/Ricevute/* ./
rm -rf Ricevute
