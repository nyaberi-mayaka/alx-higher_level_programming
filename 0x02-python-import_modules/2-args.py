#!/usr/bin/python3
def main():
    import sys
    i = len(sys.argv) - 1

    if i == 0:
        print("{0:d} {1:s}".format(i, "arguments."))
    elif i > 0:
        print("{0:d} {1:s}\
{2:s}".format(i, "argument", ":" if i == 1 else "s:"))

    for i, strs in enumerate(sys.argv):
        if i == 0:
            continue
        print("{0:d}: {1:s}".format(i, strs))


if __name__ == "__main__":
    main()
