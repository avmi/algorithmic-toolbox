# Uses python3

import sys


def compute_min_refills(distance, tank, stops):
    min, prev, next = 0, 0, 0

    stops.insert(0, 0)
    stops.append(distance)

    while next < len(stops):
        if stops[next] - stops[prev] < tank:
            next += 1
        else:
            if next == prev + 1:
                return -1
            else:
                min += 1
                prev = next - 1

    return min


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())

    print(compute_min_refills(d, m, stops))