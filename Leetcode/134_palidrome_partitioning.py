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
            return res

        def is_pali(s, i, j):
            sub_str = s[i:j+1]
            return sub_str == sub_str[::-1]
        
        return backtracking(0)
    
a = "aab"
s = Solution()
print(s.partition(a))

# The time complexity of this code is O(n * 2^n), where n is the length of the input string s. This is because the backtracking function generates all possible partitions of the input string, which is of size 2^n. For each partition, the is_pali function checks if it is a palindrome, which takes O(n) time. Therefore, the total time complexity is O(n * 2^n).

# The space complexity of this code is also O(n * 2^n), since the backtracking function generates all possible partitions, each of which has a length of up to n. The res and path lists also contribute to the space complexity, but since they are cleared after each recursive call, their total space usage is proportional to the number of partitions generated, which is 2^n. Therefore, the space complexity is O(n * 2^n).