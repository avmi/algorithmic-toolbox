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


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_quick(a, b))
