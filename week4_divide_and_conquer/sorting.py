# Uses python3
import sys
import random
from __future__ import print_function


def partition3(a, l, r):
    pivot = a[l]
    i = l
    lt = l
    gt = r
    while i <= gt:
        if a[i] < pivot:
            a[i], a[lt] = a[lt], a[i]
            lt += 1
            i += 1
        elif a[i] > pivot:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1

    return lt, gt


def partition3_bessie(a, l, r):
    compare = a[l]
    smaller_index = l
    equal_index = l + 1
    larger_index = r

    while equal_index < larger_index:
        if a[equal_index] < compare:
            smaller_index += 1
            a[smaller_index], a[equal_index] = a[equal_index], a[smaller_index]
            larger_index += 1
        elif a[equal_index] > compare:
            a[equal_index], a[larger_index] = a[larger_index], a[equal_index]
            larger_index -= 1
        else:
            equal_index += 1

    return smaller_index, larger_index


def partition2(a, l, r):
    x = a[l]
    j = l

    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]

    return j


def partition2_bessie(a, l, r):
    j = l

    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]

    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]

    mid1, mid2 = partition3(a, l, r)
    randomized_quick_sort(a, l, mid1 - 1)
    randomized_quick_sort(a, mid2 + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    a = data[1:]
    randomized_quick_sort(a, 0, n - 1)

    for x in a:
        print(x, end=' ')
