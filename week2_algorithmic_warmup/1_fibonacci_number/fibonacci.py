# Uses python3
def calc_fib(n):
    if n <= 1:
        return n

    prev = 0
    cur = 1

    for _ in range(n - 1):
        prev, cur = cur, prev + cur

    return cur


n = int(input())
print(calc_fib(n))
