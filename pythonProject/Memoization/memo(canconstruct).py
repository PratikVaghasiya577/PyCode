def canconstruct(targetstr: str, wordbank, cache={}):
    if targetstr in cache:
        return cache[targetstr]
    if targetstr == '':
        return True
    for word in wordbank:
        if targetstr.startswith(word):
            suffix = targetstr[len(word):]
            if canconstruct(suffix, wordbank, cache):
                cache[targetstr] = True
                return True
    cache[targetstr] = False
    return False


def canconstruct_recur(targetstr: str, wordbank):
    if targetstr == '':
        return True
    for word in wordbank:
        if targetstr.startswith(word):
            suffix = targetstr[len(word):]
            if canconstruct(suffix, wordbank):
                return True
    return False


print(canconstruct('abcdeeeeeeeeeeeeeef', ['ee','ab', 'cd', 'de', 'ef']))
