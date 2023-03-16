class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        j = 0
        i = 0

        while j < len(abbr) and i < len(word):
            if abbr[j] == word[i]:
                j += 1
                i += 1
            elif abbr[j] == "0":
                return False 

            elif abbr[j].isdigit():

                num_str = ""
                while j <len(abbr) and abbr[j].isdigit():
                    num_str = num_str + abbr[j]
                    j += 1

                i += int(num_str)
            else:
                return False 

        return i == len(word) and j ==len(abbr)

# time complexity: O(N)
# space complexity: O(1)
    


    
    
    
    
word = "internationalization"
abbr = "i5a11o1"
s = Solution()
print(s.validWordAbbreviation(word, abbr))