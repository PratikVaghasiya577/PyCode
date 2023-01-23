def countconstruct(targetstr: str, wordbank, memo={}):
    if targetstr in memo:
        return memo[targetstr]
    if targetstr == '':
        return 1
    count = 0
    for word in wordbank:
        if targetstr.startswith(word):
            numways = countconstruct_recur(targetstr[len(word):], wordbank)
            count += numways
    memo[targetstr] = count
    return count


def countconstruct_recur(targetstr: str, wordbank):
    if targetstr == '':
        return 1
    count = 0
    for word in wordbank:
        if targetstr.startswith(word):
            numways = countconstruct_recur(targetstr[len(word):], wordbank)
            count += numways
    return count


print(countconstruct_recur('eeeeeeeeeeeeeeeprle', ['e', 'ee', 'pu', 'p', 'r', 'le']))


def allconstruct_recurs(targetstr: str, wordbank):
    result = []
    if targetstr == '':
        return [[]]
    for word in wordbank:
        if targetstr.startswith(word):
            suffix = targetstr[len(word):]
            suffixways = allconstruct(suffix, wordbank)
            targetways = list(map(lambda l: l + [word], suffixways))
            result.extend(targetways)
    return result


def allconstruct(targetstr: str, wordbank, cache={}):
    result = []
    if targetstr in cache:
        return cache[targetstr]
    if targetstr == '':
        return [[]]
    for word in wordbank:
        if targetstr.startswith(word):
            suffix = targetstr[len(word):]
            suffixways = allconstruct(suffix, wordbank)
            targetways = list(map(lambda l: l + [word], suffixways))
            result.extend(targetways)
    cache[targetstr] = result
    return result


print(allconstruct('eeeeeeeeeeeeeeeprle', ['e', 'ee', 'pu', 'p', 'r', 'le']))
