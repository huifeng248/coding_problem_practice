class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def backtracking(i):
            if i >= len(s):
                res.append(path.copy())
                return 
            
            for j in range(i, len(s)):
                if is_pali(s, i, j):
                    path.append(s[i:j+1])
                    backtracking(j+1)
                    path.pop()
            
            return res

        def is_pali(s, i, j):
            sub_str = s[i:j+1]
            return sub_str == sub_str[::-1]
        
        return backtracking(0)