import sys


def add(n1, n2):
    return n1 + n2


def minus(n1, n2):
    return n1 - n2


def multi(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def modulo(n1, n2):
    return n1 % n2


if len(sys.argv) <= 2:
    print("Usage: python3 operations.py <number1> <number2>")
    print("Example:")
    print("\tpython3 operations.py 10 3")
elif len(sys.argv) > 3:
    print("InputError: too many arguments")
else:
    try:
        n1 = int(sys.argv[1])
        n2 = int(sys.argv[2])
        sum = add(n1, n2)
        difference = minus(n1, n2)
        product = multi(n1, n2)
        if n2 == 0:
            quotient = "ERROR (div by zero)"
            remainder = "ERROR (modulo by zero)"
        else:
            quotient = divide(n1, n2)
            remainder = modulo(n1, n2)
        print("Sum:\t\t", str(sum))
        print("Difference:\t", str(difference))
        print("Product:\t", str(product))
        print("Quotient:\t", str(quotient))
        print("Remainder:\t", str(remainder))
    except ValueError:
        print("InputError: only numbers")
