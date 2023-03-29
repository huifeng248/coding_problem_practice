class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        word_1 = []
        for i, char in enumerate(s):
            if char == "#":
                if word_1:
                    word_1.pop()
            else:
                word_1.append(char)
        
        word_2 = []
        for i, char in enumerate(t):
            if char == "#":
                if word_2:
                    word_2.pop()
            else:
                word_2.append(char)
        
        return word_1 == word_2

# Time Complexity: O(M+N), where M,NM, NM,N are the lengths of S and T respectively.

# Space Complexity: O(M+N).