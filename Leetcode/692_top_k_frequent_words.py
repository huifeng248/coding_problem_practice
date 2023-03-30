from collections import Counter
from heapq import heapify, heappop
# use hash map
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_dict = {}
        for word in words:
            word_dict[word] = word_dict.get(word, 0)+1
        
        key_value_pairs = word_dict.items()
        # sorted the set nested in a List
        # need to remember this!!!! sorted!!!
        sorted_pairs = sorted(key_value_pairs, key=lambda x: (-x[1], x[0]))
        res = []
        for i in range(k):
            res.append(sorted_pairs[i][0])
        return res        

# time complexity: O(nlog(n)) mainly for the sorting sorted_pairs, We count the frequency of each word in O(N)O(N)O(N) time, and then we sort the given words in O(Nlog⁡N)O(N \log{N})O(NlogN) time.
# space complexity: O(n) 

# use heap
class Solution:
    def topKFrequent(self, words: List[str], k:int) -> List[str]:
        count = Counter(words)
        word_heap = [(-pair[1], pair[0]) for pair in count.items()]
        heapify(word_heap)

        res = []
        for i in range(k):
            key = heappop(word_heap)[1]
            res.append(key)
        return res

# Time Complexity: O(N+klog⁡N). We count the frequency of each word in O(N) time and then heapify the list of unique words in O(N)time. Each time we pop the top from the heap, it costs log⁡N\log{N}logN time as the size of the heap is O(N).

# Space Complexity: O(N), the space used to store our counter cnt and heap h.


