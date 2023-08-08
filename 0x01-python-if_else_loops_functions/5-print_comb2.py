#!/usr/bin/python3
for i in range(0, 99):
    if len(str(i)) == 1:
        print("0{}".format(i), end=', ')
    else:
        print("{}".format(i), end=', ')
print(99)
