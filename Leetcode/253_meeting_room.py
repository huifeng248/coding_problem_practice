class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        used_room = 0

        start_times = sorted([i[0] for i in intervals])
        end_times = sorted([i[1] for i in intervals])

        s = 0
        e = 0
        length = len(intervals)
        # print("ll", length)
        while s < length:
#   when the start is greater then the end, means room is free up, no need to open a new room  
          if start_times[s] >= end_times[e]:
                s += 1
                e += 1
          else:
              used_room += 1
              s += 1
        return used_room
