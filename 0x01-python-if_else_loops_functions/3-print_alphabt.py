#!/usr/bin/python3
for character in range(97, 123):
    if character != ord('q') and character != ord('e'):
        print("{}".format(chr(character)), end='')
