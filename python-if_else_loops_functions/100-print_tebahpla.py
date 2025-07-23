#!/usr/bin/python3
print("{}".format("".join(
    chr(i + 32) if i % 2 else chr(i)
    for i in range(90, 64, -1)
)), end="")
