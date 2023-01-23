def fib(n, cache={}):
    """
    returns fib number

    :param n: input
    :param cache: does the memoization and returns the value to minimize the operation time
    takes O(n) time
          O(n) space
    """
    if n in cache:
        return cache[n]
    if 0 < n <= 2:
        return 1
    a = fib(n - 1) + fib(n - 2)  # recursion
    cache[n] = a
    return cache[n]


def fib_recurs(n):
    """
    recursive approach
    :param n: input
    takes O(2^n) time
          O(n) space
    """
    if 0 < n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)  # recursion


print(fib(50))
print(fib_recurs(32))
