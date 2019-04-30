# Uses python3
from __future__ import print_function
import math
import sys


def binary_search(a, x):
    left, right = 0, len(a) - 1

    while left <= right:
        mid = left + ((right - left) // 2)

        if x == a[mid]:
            return mid
        elif x > a[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


def binary_search_his(a, x):
    left, right = 0, len(a) - 1

    while left <= right:
        mid = left + (right - left) // 2

        a_mid = a[mid]
        if x == a_mid:
            return mid

        if a_mid < x:
            left = mid + 1

        elif x < a_mid:
            right = mid - 1

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]

    for x in data[n + 2:]:
        print(binary_search(a, x), end=' ')
