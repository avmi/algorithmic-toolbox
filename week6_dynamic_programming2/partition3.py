# Uses python3
import sys
import itertools


def partition3(a):
    if len(a) < 3:
        return 0
    elif sum(a) % 3 == 0:
        W = sum(a) // 3
    else:
        return 0

    count = 0
    d = [[0 for _ in range(W + 1)] for _ in range(len(a) + 1)]

    for item in range(1, len(a) + 1):
        for capacity in range(1, W + 1):
            d[item][capacity] = d[item - 1][capacity]

            if a[item - 1] <= capacity:
                temp_value = d[item - 1][capacity - a[item - 1]] + a[item - 1]
                if temp_value > d[item][capacity]:
                    d[item][capacity] = temp_value

            if d[item][capacity] == W:
                count += 1

    return 1 if count >= 3 else 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))
