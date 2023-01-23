def stribgcomp(s):
    r = ''
    count = 1
    l = len(s)
    if l == 0:
        return 0
    if l == 1:
        return s + '1'
    i = 1
    while i < l:
        if s[i] == s[i - 1]:
            count += 1

        else:
            r += s[i - 1] + str(count)
        i += 1

    r += s[i - 1] + str(count)
    return r


print(stribgcomp('AABBC'))
