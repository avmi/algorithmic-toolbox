# Uses python3
import sys


def count_segments(starts, ends, points):
    cnt = [0] * len(points)
    points_num = [i for _, i in sorted(zip(points, range(len(points))))]

    full = [(p, 1) for p in points]
    full.extend([(s, 0) for s in starts])
    full.extend([(e, 2) for e in ends])

    full.sort()

    num_open_segments = 0
    i = 0

    for val, p_type in full:
        if p_type == 0:
            num_open_segments += 1
        elif p_type == 2:
            num_open_segments -= 1
        else:
            cnt[points_num[i]] = num_open_segments
            i += 1

    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    m = data[1]

    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]

    cnt = count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
