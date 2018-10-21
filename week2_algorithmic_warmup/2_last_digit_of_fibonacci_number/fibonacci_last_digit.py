# Uses python3
import sys

def get_fibonacci_last_digit_fast(n):
    if n <= 1:
        return n

    prev = 0
    cur = 1

    for _ in range(n - 1):
        prev, cur = cur % 10, (prev + cur) % 10

    return cur


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_fast(n))
