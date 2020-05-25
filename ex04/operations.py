import sys


def operations(n1, n2):
    if n2 == 0:
        quotient = "ERROR (div by zero)"
        remainder = "ERROR (modulo by zero)"
    else:
        quotient = str(n1 / n2)
        remainder = str(n1 % n2)

    return (n1 + n2, n1 - n2, n1 * n2, quotient, remainder)


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
        results = operations(n1, n2)
        print("""Sum:\t\t%d
Difference:\t%d
Product:\t%d
Quotient:\t%s
Remainder:\t%s""" % results)
    except ValueError:
        print("InputError: only numbers")
