def cansum_tab(target: int, nums):
    """
    O(mn) time
    O(m) space
    :param target:
    :param nums:
    :return:
    """
    table = [False] * (target + 1)
    table[0] = True
    for i in range(len(table)):
        for num in nums:
            print('%s'%table)
            if table[i] is True and i+num < len(table):
                table[i+num] = True
    return table[target]


print(cansum_tab(7, [3, 5]))
