class Solution:
    def partition(self, s):
        res = []
        path = []
        def backtracking(i):
            if i >= len(s):
                res.append(path.copy())
                return 
            
            for j in range(i, len(s)):
                print("j", j, "i", i, "path", path, "res", res)
                if is_pali(s, i, j):
                    path.append(s[i:j+1])
                    print("path~~~", path)
                    backtracking(j+1)
                    print("come", path)
                    popped = path.pop()
                    print("come here", path, "popped", popped)

                print("outside~~~~~~~~", s[i:j+1], "res", res)
            

        def is_pali(s, i, j):
            sub_str = s[i:j+1]
            return sub_str == sub_str[::-1]
        
        backtracking(0)
        return res
    
a = "ab"
s = Solution()
print(s.partition(a))

# The time complexity of this code is O(n * 2^n), where n is the length of the input string s. This is because the backtracking function generates all possible partitions of the input string, which is of size 2^n. For each partition, the is_pali function checks if it is a palindrome, which takes O(n) time. Therefore, the total time complexity is O(n * 2^n).


# Space Complexity: O(N)\mathcal{O}(N)O(N), where NNN is the length of the string sss. This space will be used to store the recursion stack. For s = aaa, the maximum depth of the recursive call stack is 3 which is equivalent to NNN.