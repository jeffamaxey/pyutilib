#!/usr/bin/env python
#
# A script that verifies that suitable copyright statements are 
# defined in files.
#

import sys
import os
import re

suffixes = ['.c', '.cc', '.h', '.H', '.cpp', '.py']


def recurse(dir):
    for root, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            for suffix in suffixes:
                if filename.endswith(suffix):
                    yield os.path.join(root, filename)


def match(filename, pat):
    with open(filename, 'r') as INPUT:
        fstring = INPUT.read()
    return bool(pat.search(fstring))


def main():
    nfiles = 0
    badfiles = []
    if sys.argv[1] == '-c':
        cfile = sys.argv[2]
        files = sys.argv[3:]
        with open(cfile, 'r') as INPUT:
            cstring = INPUT.read()
        pat = re.compile(cstring)
    else:
        cfile = None
        cstring = None
        pat = re.compile('Copyright')
        files = sys.argv[1:]
    for dir_ in files:
        for filename in recurse(dir_):
            nfiles += 1
            if not match(filename, pat):
                badfiles.append(filename)

    print(f"Total number of files missing copyright: {len(badfiles)}")
    print(f"Total number of files checked:           {str(nfiles)}")
    if badfiles:
        print("")
        print("Bad Files")
        print("-" * 40)
        for filename in badfiles:
            print(filename)


if __name__ == '__main__':
    main()
