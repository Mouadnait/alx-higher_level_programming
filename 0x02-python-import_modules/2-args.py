#!/usr/bin/python3
import sys
if __name__ == '__main__':
    len_argv = len(sys.argv) - 1
    if len_argv == 1:
        print("{} argument:".format(len_argv))
        print("{}: {}".format(len_argv, sys.argv[len_argv]))
    else:
        print("{} arguments:".format(len_argv))
        print("".join('{}: {}\n'.format(num, sys.argv[num])
                      for num in range(1, len_argv + 1)), end='')
