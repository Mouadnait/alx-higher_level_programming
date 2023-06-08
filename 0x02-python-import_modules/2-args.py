#!/usr/bin/python3
import sys
if __name__ == "__main__":
    res = ""
    argc = len(sys.argv) - 1
    delim = 's:' if argc > 1 else '.' if argc == 0 else ':'
    print("{} arguments{}".format(argc, delim))
    for i, arg in enumerate(sys.argv):
        if i > 0:
            res += '{:d}: {}\n'.format(i, arg)
    print("{}".format(res))
