# Uses python3

import sys


def isGreaterOrEqual(digit, max):
    d = int(str(digit)+str(max))
    m = int(str(max)+str(digit))

    return (d >= m)



def largest_number(a):
    res = ""

    r=[]
    while a != []:
        max = 0
        for digit in a:
            if isGreaterOrEqual(digit,max):
                max = digit

        r.append(max)
        a.remove(max)

    for rr in r:
        res += str(rr)

    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))