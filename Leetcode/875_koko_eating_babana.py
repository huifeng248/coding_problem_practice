class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_num = max(piles)
        min_num = 1
    
        ans = float('inf')
        while min_num <= max_num:
            mid_p = (max_num + min_num)//2
            
            used_time = self.calculate_time(mid_p, piles)
            if used_time > h:
                min_num = mid_p + 1
            else:
                ans = min (ans, mid_p)
                max_num = mid_p -1   
        return ans


    
    def calculate_time(self, k, piles):
        res = 0
        for pile in piles:
            whole, remainder = divmod(pile, k)
            if remainder == 0:
                res += whole
            else:
                res += (whole+1)
        return res 

       