# System modules
import os, sys, subprocess
import argparse

from os_lib import getfiles_walk

# Parse arguments
parser = argparse.ArgumentParser(description='Looking through folders')
parser.add_argument('pwd', type=str)
args = parser.parse_args()
searchPath = args.pwd

# Get all python files in that folder
pathPairs = getfiles_walk(searchPath, exts=['.py'])
paths = [os.path.join(a, b) for a,b in pathPairs]

# For each file, extract lines with first word 'import'
# Extract only 2nd word
# FIXME: Delete all comments from a file prior to reading, as some comments may end up looking like a dependency
linesRez = []
for p in paths:
    with open(p, 'r') as f:
        lines = f.readlines()

        for l in lines:
            l = l.strip()
            if l[:7] == 'import ':
                # print(' ' in l, l)
                linesRez += [l.split(' ')[1].split(',')[0].split('.')[0]]
            elif l[:5] == 'from ':
                linesRez += [l.split(' ')[1].split(',')[0].split('.')[0]]

            if linesRez[-1] == 'mat':
                print(l)

# Keep only unique
linesRez = list(sorted(set(linesRez)))

print(linesRez)
