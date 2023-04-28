from collections import Counter
from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        queue = deque() # pairs of [-cnt, idletime]
        
        # while we have sth to process
        while maxHeap or queue:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt != 0:
                    queue.append([cnt, time+n])

            if queue and queue[0][1] == time:
                temp = queue.popleft()
                heapq.heappush(maxHeap, temp[0])
        return time                   

# time complexity: O(n)
# space complexity: O(n) 

import heapq
heapq.heapify(maxHeap)
heapq.heappush(maxHeaq, count)
Heapq.heappop(maxHeaq)





