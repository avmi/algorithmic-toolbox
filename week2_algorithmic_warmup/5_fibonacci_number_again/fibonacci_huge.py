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


def get_fibonacci_huge_quick(n, m):
    rem = n % fib_period(m)
    return fib(rem) % m


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_quick(n, m))
