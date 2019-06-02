# Uses python3
import sys

def optimal_sequence(n):
    v = [0] * (n + 1)
    v[1] = 1

    s = []

    for i in range(1, n + 1):
        v[i] = v[i - 1] + 1

        if (i % 2) == 0:
            v[i] = min((1 + v[i // 2]), v[i])

        if (i % 3) == 0:
            v[i] = min((1 + v[i // 3]), v[i])

    while n > 1:
        s.append(n)

        if v[n - 1] == v[n] - 1:
            n = n - 1
        elif (n % 3) == 0 and v[n // 3] == v[n] - 1:
            n = n // 3
        elif (n % 2) == 0 and v[n // 2] == v[n] - 1:
            n = n // 2

    s.append(1)

    return reversed(s)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
