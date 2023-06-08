#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum_arg = 0
    for i, k in enumerate(sys.argv):
        if i != 0:
            sum_arg += int(k)
    print(sum_arg)
