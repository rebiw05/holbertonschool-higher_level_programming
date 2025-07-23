#!/usr/bin/python3
print("".join(chr(i+32 if i % 2 else i) for i in range(90, 64, -1)), end="")
