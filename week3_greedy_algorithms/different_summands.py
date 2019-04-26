# Uses python3
import sys

def optimal(k, l):
    if k <= 2*l:
        return [k]

    return [l] + optimal(k-l, l+1)


def get_summands(n):
    result = []

    for num in range(1, n+1):
        if n <= num*2:
            result.append(n)
            return result

        result.append(num)
        n -= num


if __name__ == '__main__':
    input = input()
    n = int(input)

    summands = get_summands(n)
    print(len(summands))

    for x in summands:
        print(x, end=' ')