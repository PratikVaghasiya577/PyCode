def howsum_tab(target, nums):
    table = [None] * (target + 1)
    table[0] = []
    for i in range(len(table)):
        for num in nums:
            if table[i] is not None and i + num < len(table):
                table[i + num] = table[i] + [num]
            print('%s' % table)
    return table[target]


def bestsum_tab(target, nums):
    table = [None] * (target + 1)
    table[0] = [[]]

    for i in range(len(table)):
        for num in nums:
            if table[i] is not None and i + num < len(table):
                combination = table[i] + [num]
                table[i + num] = table[i] + [num]
                a = list(map(combination,table[i+num]))
                table.extend(a)


            print('%s' % table)
    return table[target]


print(bestsum_tab(7, [3, 2, 7]))
