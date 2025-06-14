#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= ord('A') and ord(c) <= ord('Z'):
            c = chr(ord(c)-32)
        print("{}".format(c), end="")
    print()
