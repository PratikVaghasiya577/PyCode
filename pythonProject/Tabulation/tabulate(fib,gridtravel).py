def fib_tab(n):
    """
    O(n) time
    O(n+2) space
    """
    table = [0] * (n + 2)
    table[1] = 1
    for i in range(n):
        # print('%s'%table)
        table[i + 2] += table[i]
        table[i + 1] += table[i]
    return table[n]


print(fib_tab(500))


def gridtraveller_tab(m, n):
    """
    O(n) time
    O(n*m) space
    :param m:
    :param n:
    :return:
    """
    table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    table[1][1] = 1  # base case
    for i in range(m + 1):
        for j in range(n + 1):
            current = table[i][j]
            if j + 1 <= n:
                table[i][j + 1] += current
            if i + 1 <= m:
                table[i + 1][j] += current
    return table[m][n]


print(gridtraveller_tab(2, 2))
