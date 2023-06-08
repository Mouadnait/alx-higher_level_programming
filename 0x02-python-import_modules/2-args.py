#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv) - 1
    print("{} arguments.".format(argc))
    for i, arg in enumerate(sys.argv):
        if i > 0:
            print("{}: {}".format(i, arg))
