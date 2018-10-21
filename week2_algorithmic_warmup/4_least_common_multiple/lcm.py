# Uses python3
import sys


def gcd_quick(a, b):
    divisor = a if (a <= b) else b
    dividend = a if (a >= b) else b

    while divisor != 0:
        rem = dividend % divisor
        dividend = divisor
        divisor = rem

    return dividend


def lcm_quick(a, b):
    return (a * b) // gcd_quick(a, b)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_quick(a, b))
