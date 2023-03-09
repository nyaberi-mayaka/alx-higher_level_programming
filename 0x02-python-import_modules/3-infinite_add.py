#!/usr/bin/python3
def main():
    import sys

    if len(sys.argv) == 1:
        print("{:d}".format(0))

    else:
        result = 0

        for i, strs in enumerate(sys.argv):
            if i == 0:
                continue

            result += int(strs)
        print("{:d}".format(result))


if __name__ == "__main__":
    main()
