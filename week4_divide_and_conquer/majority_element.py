# Uses python3
import sys
from functools import reduce


def get_majority_element(a, left, right):
    if right == left:
        return a[right]

    if right - left == 1:
        if a[right] == a[left]:
            return a[left]
        else:
            return -1

    mid = left + ((right - left) // 2)
    left_element = get_majority_element(a, left, mid)
    right_element = get_majority_element(a, mid + 1, right)

    if (left_element != -1) and (a[left:right + 1].count(left_element) > ((right + 1 - left) // 2)):
        return left_element
    elif (right_element != -1) and (a[left:right + 1].count(right_element) > ((right + 1 - left) // 2)):
        return right_element

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))

    if get_majority_element(a, 0, n - 1) != -1:
        print(1)
    else:
        print(0)
