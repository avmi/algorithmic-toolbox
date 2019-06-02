# Uses python3

import sys


def lcs3(a, b, c):
    x = len(a)
    y = len(b)
    z = len(c)

    d = [[[None] * (z + 1) for j in range(y + 1)] for k in range(x + 1)]

    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i == 0 or j == 0 or k == 0:
                    d[i][j][k] = 0
                elif a[i - 1] == b[j - 1] and b[j - 1] == c[k - 1]:
                    d[i][j][k] = 1 + d[i - 1][j - 1][k - 1]
                else:
                    d[i][j][k] = max(d[i - 1][j][k], d[i][j - 1][k], d[i][j][k - 1])

    return d[i][j][k]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
