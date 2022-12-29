class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        
        def get_path(beginWord, endWord, wordList):
            if endWord not in wordList:
                return 0

            word_length = len(beginWord)
            gragh = {}


            def get_neighbours(wordList, gragh):
                for word in wordList:
                    for i in range(len(word)):
                        if word[0:i]+"*"+ word[i+1: -1] not in gragh:
                            gragh[ word[0:i]+"*"+ word[i+1: ]] = []

                        gragh[ word[0:i]+"*"+ word[i+1: ]].append(word)

                return gragh

            def get_generic_word(word):
                for i in range(len(word)):
                    generic_word =  word[0:i]+"*"+ word[i+1:]
                return generic_word

            queue = collections.deque([(beginWord, 0)])
            visited = set()
            gragh = get_neighbours(wordList, gragh)
            while queue:
                current, level = queue.popleft()
                if current == endWord:
                    return level + 1
                
                visited.add(current)
                
                for i in range(len(current)):
                    generic_word =  current[0:i]+"*"+ current[i+1:]
                    
                    print("generic_word!!!", generic_word)
                    # print("gragh!!!!!", gragh)
                if generic_word in gragh:
                    print("neighbors~~~", gragh)
                    for neighbor in gragh[generic_word]:
                        if neighbor == endWord:
                            return level +1
                        if neighbor not in visited:
                            queue.append((neighbor, level+1))
                
                return 0
        return get_path(beginWord, endWord, wordList)
                                     

solution = Solution()
solution.ladderLength()