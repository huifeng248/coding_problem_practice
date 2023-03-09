class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_l = len(s)
        t_l = len(t)
        print("len", s_l)
        if not s:
            return True
        if s_l > t_l:
            return False
         
        s_p, t_p = 0, 0
        while t_p < t_l:
            
            if s[s_p] == t[t_p]:
                if s_p == s_l -1:
                    return True
                s_p += 1

            t_p += 1
        return False 

# Time Complexity: O(∣T∣)
# Space Complexity: O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

        p_left = p_right = 0
        while p_left < LEFT_BOUND and p_right < RIGHT_BOUND:
            # move both pointers or just the right pointer
            if s[p_left] == t[p_right]:
                p_left += 1
            p_right += 1

        return p_left == LEFT_BOUND

# Time Complexity: O(∣T∣)
# Space Complexity: O(1)