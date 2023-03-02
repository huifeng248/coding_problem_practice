class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        sorted_list = sorted(intervals)
        print("sorted", sorted_list)
        res = [sorted_list[0]]
        for i in range(1, len(sorted_list), 1):
            interval = sorted_list[i]
            prev_start, prev_end = res[-1]
            cur_start, cur_end = interval
            print([prev_start, prev_end], [cur_start, cur_end])
            if prev_end == cur_start:
                res[-1] = [prev_start, cur_end]
                # print("res", res)
            elif prev_end > cur_start:
                # print("@@@@", [prev_start, prev_end], [cur_start, cur_end])
                return False
            else:
                res.append([cur_start, cur_end])
        return True