# Uses python3


def edit_distance(s, t):
    m, n = len(s), len(t)
    table = [([0] * (n + 1))[:] for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                table[i][j] = j
            elif j == 0:
                table[i][j] = i
            elif s[i - 1] == t[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(table[i][j - 1], table[i - 1][j], table[i - 1][j - 1])

    return table[m][n]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
