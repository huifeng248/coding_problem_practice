def permutation(words):
    if len(words) == 0:
        return [[]]
    first = words[0]
    without_first = permutation(words[1:])
    with_first = []
    for perm in without_first:
        for i in range(len(perm)+1):
            ele = [first, *perm[:i], *perm[i:]]
            with_first.append(ele)
    return with_first

words = ["foo", "bar", "abc"]
print(permutation(words))

# ["foo", "bar"] ,["bar", "foo"]