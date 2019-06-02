# Uses python3
import sys


def get_change(m):
    denominations = [4, 3, 1]
    array_m = [0] * (m + 1)

    i = 0
    while (i <= m):
        candidates = list(map(lambda x: array_m[x], filter(lambda x: x >= 0, [i - d for d in denominations])))
        if len(candidates) > 0:
            array_m[i] = min(candidates) + 1
        else:
            array_m[i] = 0
        i += 1

    return array_m[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
