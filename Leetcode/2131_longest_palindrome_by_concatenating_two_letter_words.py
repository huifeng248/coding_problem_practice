class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        reversed = {}
        double = set()
        res = 0
        for word in words:
            if word in reversed:
                print("word", word)
                # reversed.remove(word)
                reversed[word] -=1
                if reversed[word] == 0:
                    del reversed[word]
                res += 4
                if word in double:
                    double.remove(word)
                # continue 
            else:
                reversed_word = word[::-1]
                if word == reversed_word:
                    double.add(reversed_word)
                reversed[reversed_word] = reversed.get(reversed_word, 0)+1
        if len(double) >= 1:
            res += 2

        return res


# The time complexity of this code is O(n * k), where n is the number of words in the input list and k is the average length of each word. This is because the code iterates through each word in the input list and for each word, it performs constant time operations like dictionary lookups and set operations.

# The space complexity of this code is O(n), where n is the number of words in the input list. This is because the code uses a dictionary to store the reversed words and a set to store the words that appear twice. The size of these data structures can grow up to the size of the input list. The variable res is also a constant amount of memory that doesn't depend on the input size.