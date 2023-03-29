import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #use min-heap to solve this
        #heapq.heappop() and heapq.heappush(list, ele) take log(n)
        #It does this by maintaining the items in a special order (within the array), or as a balanced binary tree.
        
        stone_negative = [-ele for ele in stones]
        heapq.heapify(stone_negative)
        # print(stone_negative)
        while len(stone_negative)>1:
            stone_1 = heapq.heappop(stone_negative)
            stone_2 = heapq.heappop(stone_negative)
            if stone_1 != stone_2:
                heapq.heappush(stone_negative, stone_1-stone_2)
        
        return -heapq.heappop(stone_negative) if stone_negative else 0


# time complexity: nlog(n)
# space complexity:n, as we create anather array 