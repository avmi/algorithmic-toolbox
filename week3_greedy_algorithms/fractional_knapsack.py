# Uses python3
import sys

def loot(capacity, weights, values):
    value = 0.
    new_list = list(map(lambda v,w : v/w, values, weights))
    wmap = dict(zip(new_list,weights))
    for item in sorted(new_list, reverse=True):
        total = item * wmap[item],
        if capacity > wmap[item]:
            capacity -= wmap[item]
            value += total
        else:
            value += capacity*item
            break

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))

    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]

    optimal_value = loot(capacity, weights, values)
    print("{:.10f}".format(optimal_value))
