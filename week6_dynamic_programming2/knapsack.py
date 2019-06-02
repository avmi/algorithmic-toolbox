# Uses python3
import sys


def optimal_weight(W, w):
    lw = len(w)

    d = [[0 for j in range(W + 1)] for i in range(lw + 1)]

    for i in range(1, lw + 1):
        for j in range(1, W + 1):
            d[i][j] = d[i - 1][j]

            if w[i - 1] <= j:
                value = d[i - 1][j - w[i - 1]] + w[i - 1]
                if d[i][j] < value:
                    d[i][j] = value

    return d[lw][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
