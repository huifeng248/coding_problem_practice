class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_dict = {}
        visited = set()
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            if char_s not in map_dict and char_t not in visited:
                map_dict[char_s] = char_t
                visited.add(char_t)
            elif char_s not in map_dict and char_t in visited:
                return False
            elif map_dict[char_s] != char_t:
                    return False 
        return True

# time complexity: O(N)
# space complexity: O(1) since the size of the ASCII character set is fixed and the keys in our dictionary are all valid ASCII characters according to the problem statement.