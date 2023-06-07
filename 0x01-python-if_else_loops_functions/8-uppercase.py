#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        print("{}".format(chr(ord(ch) - 32) if ord(ch) >= 97 and ord(ch) <= 122 else chr(ord(ch))), end='')
    print()
