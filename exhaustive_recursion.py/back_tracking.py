# def combine(n, k, start = 1, comb= []):
#     res = []
    
#     def backtrack(start, comb):
#         if len(comb) == k:
#             res.append(comb.copy())
#             return 
    
#         for i in range(start, n+1):
#             comb.append(i)
#             backtrack(i+1, comb)
#             comb.pop()
    
#     backtrack(1, [])
    
#     return res

# def combine(n, k, start = 1, comb= [], res =[]):
    
#     if len(comb) == k:
#         res.append(comb.copy())
#         print("res", res, "comb", comb)
#         return 

#     print("ssstart", start)
#     for i in range(start, n+1):
#         comb.append(i)
#         print("i", i, "res", res, "comb", comb, "start", start)
#         combine(n, k, i+1, comb, res)
#         print("ssstart~~~", start)
#         print("comb", comb)
#         comb.pop()
#         print("after pop", comb)
    
    
#     return res

def combine(n, k):
    res = []
    result = backtrack(n, k, res, start = 1, comb =[])
    return result 

def backtrack(n, k, res, start, comb):
    if len(comb) == k:
        res.append(comb.copy())
        return 
        
    for i in range(start, n+1):
        comb.append(i)  #[1]
        print("i", i, "res", res, "comb", comb, "start", start, "i+1", i+1)
        backtrack(n, k, res, i+1, comb) #[1,2]
        comb.pop() #[1]
        print("after pop", comb)
    
    return res
   
        
        

# print(combine(4, 2, 1, []))
print(combine(4, 2))

    