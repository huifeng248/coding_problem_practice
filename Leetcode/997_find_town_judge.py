class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dict_trust = {}
        has_trust = {}
        for i in range(1, n+1, 1):
            dict_trust[i] = []
            has_trust[i] = []
        for pair in trust:
            a, b = pair[0], pair[1]
            dict_trust[a].append(b)
            has_trust[b].append(a)
        
        for item in dict_trust.items():
            value = item[1]
            key = item[0]
            if len(value) == 0 and len(has_trust[key]) == n-1:
                return key
        
        return -1


# time complexity: O(n) n is the given n numbers
# space complexity: O(n) n is the given n numbers for the two hash map