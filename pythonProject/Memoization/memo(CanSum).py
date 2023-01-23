def cansum(targetsum, numbers, cache={}):
    """
    returns T if sum of elements in number can match targetsum
    One element can be used multiple time
    :param targetsum:
    :param numbers:
    takes O(mxn) time
          o(m) space
    """
    if targetsum in cache:
        return cache[targetsum]
    if targetsum == 0:
        return True
    if targetsum < 0:
        return False
    for num in numbers:
        remainder = targetsum - num
        if cansum(remainder, numbers) is True:
            cache[targetsum] = True
    cache[targetsum] = False
    return False


def cansum_recurs(targetsum, numbers):
    """
    returns T if sum of elements in number can match targetsum
    One element can be used multiple time
    :param targetsum:
    :param numbers:
    takes O(n^m)time
          O(m) space
    """
    if targetsum == 0:
        return True
    if targetsum < 0:
        return False
    for num in numbers:
        remainder = targetsum - num
        if cansum_recurs(remainder, numbers) is True:
            return True
    return False


a = 300
b = [7, 14]
print(cansum_recurs(a, b))
