# Uses python3
from sys import stdin


def fib_last_digit(n):
    if (n < 1):
        return n

    prev = 0
    cur = 1

    for _ in range(n - 1):
        prev, cur = cur % 10, (prev + cur) % 10

    return cur % 10


def fib_sum_squares_quick(n):
    y = fib_last_digit(n % 60)
    x = fib_last_digit((n + 1) % 60)

    return (y * x) % 10


if __name__ == '__main__':
    n = int(stdin.read())
    print(fib_sum_squares_quick(n))
