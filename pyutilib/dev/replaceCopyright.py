#!/usr/bin/env python
#
# A script that replaces copyright statements in files with a
# new copyright statement
#
# replaceCopyright old new file [file...]
#

import sys
import os


def match_head(file, lines):
    INPUT = open(file)
    i = 0
    for line in INPUT:
        if line.strip() != lines[i].strip():
            return False
        i = i + 1
        if i == len(lines):
            break
    return True


def main():
    with open(sys.argv[1]) as INPUT:
        old_cr = INPUT.readlines()
    for i in range(0, len(old_cr)):
        old_cr[i] = old_cr[i].strip()

    with open(sys.argv[2]) as INPUT:
        new_cr = INPUT.readlines()
    #print old_cr
    #print ""
    #print new_cr

    for file in sys.argv[3:]:
        with open(file) as INPUT:
            with open(f"{file}.tmp", "w") as OUTPUT:
                i = 0
                newfile = True
                for line in INPUT:
                    if i == len(old_cr):
                        #
                        # Print new copyright
                        #
                        for crline in new_cr:
                            OUTPUT.write(crline)
                        i = i + 1
                    if i > len(old_cr):
                        #
                        # Print lines from the old file
                        #
                        OUTPUT.write(line)
                    elif line.strip() == old_cr[i]:
                        i = i + 1
                    else:
                        INPUT.close()
                        if match_head(file, new_cr):
                            print(f"File {file} is up to date.")
                        else:
                            print("Unexpected line in file %s\n" % file)
                            print("  Expected line:\n")
                            print(old_cr[i] + '\n')
                            print("  Current line:\n")
                            print(line)
                        newfile = False
                        break
        if newfile:
            os.remove(file)
            os.rename(f"{file}.tmp", file)
            print("Updating file %s\n" % file)
        else:
            os.remove(f"{file}.tmp")


if __name__ == '__main__':
    main()
