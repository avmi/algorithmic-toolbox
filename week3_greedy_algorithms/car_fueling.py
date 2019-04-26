# Uses python3

import sys


def compute_min_refills(distance, tank, stops):
    if distance <= tank:
        return 0

    start = 0
    refuels = 0

    for i in range(len(stops)):
        stop = False

        while stops[i] - start <= tank:
            i += 1
            stop = True
            if i == len(stops):
                break

        if stop:
            start = stops[i-1]
            refuels += 1
            if start + tank >= distance:
                return refuels
        else:
            return -1

    return -1


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())

    print(compute_min_refills(d, m, stops))