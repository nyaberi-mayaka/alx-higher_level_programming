#!/usr/bin/python3
def main():
    from calculator_1 import add, sub, mul, div
    from sys import argv

    def checkops(strs):
        if len(strs) != 1:
            return (0)
        else:
            if strs == "+":
                return (1)
            elif strs == "-":
                return (1)
            elif strs == "*":
                return (1)
            elif strs == "/":
                return (1)
            else:
                return (0)

    if len(argv) != 4:
        print("./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    elif checkops(argv[2]) == 0:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == '/':
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        elif argv[2] == '+':
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif argv[2] == '-':
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif argv[2] == '*':
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))


if __name__ == "__main__":
    main()
