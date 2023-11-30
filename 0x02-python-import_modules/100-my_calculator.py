#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    nargs = len(sys.argv) - 1
    if nargs != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = sys.argv[2]
    if op != '+' and op != '-' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    from calculator_1 import addition, subtraction, multiplication, division
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if op == '+':
        print("{} + {} = {}".format(a, b, addition(a, b)))
    elif op == '-':
        print("{} - {} = {}".format(a, b, subtraction(a, b)))
    elif op == '*':
        print("{} * {} = {}".format(a, b, multiplication(a, b)))
    else:
        print("{} / {} = {}".format(a, b, division(a, b)))
