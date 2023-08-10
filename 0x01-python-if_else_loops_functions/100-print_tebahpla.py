#!/usr/bin/python3
for char in range(65, 91, 2)[::-1]:
    print("".join(reversed(chr(char) + chr((char + 1) + 32))), end='')
