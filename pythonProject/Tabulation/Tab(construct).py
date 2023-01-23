def canconstruct_tab(targetstr, words):
    """
    o(m^2n) time
    o(m) space
    :param targetstr:
    :param words:
    :return:
    """
    table = [False] * (len(targetstr) + 1)
    table[0] = True
    for i in range(len(table)):
        for word in words:
            if table[i]:
                # print('%s' % word, i)
                if targetstr[i:i + len(word)] == word:
                    table[i + len(word)] = True
                    # print('%s' % table)
    return table[len(targetstr)]


# print(canconstruct_tab('abcde', ['ab', 'cd', 'e']))


def countconstruct_tab(targetstr, words):
    """
    o(m^2n) time
    o(m) space
    """
    table = [0] * (len(targetstr) + 1)
    table[0] = 1
    for i in range(len(table)):
        for word in words:
            if table[i]:
                if targetstr[i:i + len(word)] == word:
                    table[i + len(word)] += table[i]
                    print('%s' % table)
    return table[len(targetstr)]


# print(countconstruct_tab('purple', ['purp', 'p', 'ur', 'le', 'purpl']))


def allconstruct_tab(targetstr,words):
    table = [[None for j in range(1)] for i in range(len(targetstr)+1)]
    table[0] = []
    print('%s'%table)
    # for i in range(len(table)):
    #     if table[i] is not None:
    #         for word in words:


    return table[len(targetstr)]


print(allconstruct_tab('abcde',['a','ab']))
