class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        return self.find_happiness(n, visited)
    

    def find_happiness(self, n, visited):
        if n == 1:
            return True
        if n in visited:
            return False

        n = str(n)
        sub_totle = 0
        for num in n:
            sub_totle += int(num)** 2
        
        if sub_totle == 1: return True
        

        visited.add(int(n))
        return self.find_happiness(sub_totle, visited)
        

        
s = Solution()
print(s.isHappy(2))