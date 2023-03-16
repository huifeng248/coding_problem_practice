# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n <= 1:
            return n
        min_i = 1
        max_i = n
        while min_i < max_i:
            
            mid = (min_i + max_i)//2
            # print("mid", mid, isBadVersion(mid))
            if not isBadVersion(mid):
                if isBadVersion(mid+1):
                    return mid + 1
                min_i = mid + 1
                
            else: 
                
                max_i = mid
        # print(min_i == max_i) this is true, cause min_i would move to max_i, thus return max_i or min_i is the same
        
        return min_i

# time complexity: O(log(n))
# space complexity:O(1)
        

            