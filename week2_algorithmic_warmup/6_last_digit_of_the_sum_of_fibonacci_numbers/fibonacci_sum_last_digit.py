# Uses python3
import sys


def fib_last_digit(n):
    if n <= 1:
        return n

    prev = 0
    cur = 1

    for _ in range(n - 1):
        prev, cur = cur % 10, (prev + cur) % 10

    return cur


def fibonacci_sum_quick(n):
    last = fib_last_digit((n + 2) % 60)

    if last == 0:
        return 9
    else:
        return last - 1


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_quick(n))
