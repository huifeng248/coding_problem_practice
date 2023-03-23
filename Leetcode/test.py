def pop_arr(a, b):
    res = 0
    while a and b:
        if a[-1] == b[-1]:
            res = a.pop()
            b.pop()
    print("a", a)
    print("b", b)
    return res
    
a = [3, 5]
b = [1, 3, 5]

print(pop_arr(a, b))