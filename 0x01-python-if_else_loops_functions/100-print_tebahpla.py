#!/usr/bin/python3
for ch in reversed(range(97, 123)):
    print("{:s}".format(chr(ch) if (ch % 2 == 0) else chr(ch - 32)), end="")
