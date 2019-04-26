# Uses python3
import sys

def loot(capacity, weights, values):
    value = 0
    pairs = sorted(list(zip(weights, values)), key = lambda x:x[1]/x[0], reverse=True)

    for (w, v) in pairs:
        if capacity - w >= 0:
            value += v
            capacity -= w
        else:
            value += (v / w) * capacity
            capacity = 0
        if not capacity:
            break

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))

    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]

    optimal_value = loot(capacity, weights, values)
    print("{:.10f}".format(optimal_value))
