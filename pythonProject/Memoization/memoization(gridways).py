def ways(i, j, cache=None):
    """
    code returns maximum number of ways to reach at right bottom of mxn matrix
    :param i: row
    :param j: column
    :param cache: memoization (stores value of the key(m,n) which can be used later on
    takes O(mxn) time
          O(m + n) space

    """
    if cache is None:
        cache = {}
    key = chr(i) + ',' + chr(j)
    if key in cache:
        return cache[key]
    if i < 1 and j < 1:  # base case
        return 0
    elif i == 1 or j == 1:  # base case
        return 1
    cache[key] = ways(i - 1, j) + ways(i, j - 1)  # recursion
    return cache[key]


def ways_recur(i, j):
    """
    recursive approach
    takes O(2^(m+n)) time
          O(M+N) space
    """
    if i < 1 and j < 1:
        return 0
    elif i == 1 or j == 1:
        return 1
    return ways_recur(i - 1, j) + ways_recur(i, j - 1)


print(ways(3, 7))
