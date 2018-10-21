# Uses python3
import sys


def fib(n):
    if n <= 1:
        return n

    prev = 0
    cur = 1

    for _ in range(n - 1):
        prev, cur = cur, prev + cur

    return cur


def fib_period(m):
    prev = 0
    cur = 1

    for i in range(m * m + 1):
        prev, cur = cur, (prev + cur) % m

        if prev == 0 and cur == 1:
            return i + 1


def fib_huge(n, m):
    rem = n % fib_period(m)
    return fib(rem) % m


def fib_last_digit(n):
    if n <= 1:
        return n

    prev = 0
    cur = 1

    for _ in range(n - 1):
        prev, cur = cur % 10, (prev + cur) % 10

    return cur


def fib_partial_sum_quick(from_, to):
    if from_ == to:
        return fib_last_digit(from_ % 60)
    else:
        from_ %= 60
        to %= 60

        last_from = fib_huge(from_ + 1, 10) - 1
        last_to = fib_huge(to + 2, 10) - 1

    return (last_to - last_from) % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fib_partial_sum_quick(from_, to))