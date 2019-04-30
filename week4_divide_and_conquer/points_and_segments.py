# Uses python3
from __future__ import print_function
from itertools import chain
import sys


def count_segments(starts, ends, points):
    cnt = [0] * len(points)

    st = zip(starts, ["l"] * len(starts))
    et = zip(ends, ["r"] * len(ends))
    pt = zip(points, ["p"] * len(points), range(len(points)))

    result = chain(st, et, pt)
    result = sorted(result, key=lambda a: (a[0], a[1]))

    count = 0
    for num, letter, index in result:
        if letter == 'p':
            count += 1
        elif letter == 'r':
            count -= 1
        else:
            cnt[index] = count

    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    m = data[1]

    starts = data[2:2 * n + 1:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]

    for x in count_segments(starts, ends, points):
        print(x, end=' ')
