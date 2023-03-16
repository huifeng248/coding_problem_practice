class Solution:
    def judgeCircle(self, moves: str) -> bool:
        arrs = []
        for move in moves:
            if move == "U":
                arrs.append([-1, 0])
            elif move == "D":
                arrs.append([1,0])
            elif move == "L":
                arrs.append([0, -1])
            elif move =="R":
                arrs.append([0, 1])
        print(arrs)
        row, col = 0, 0
        for pos in arrs:
            r_delta, col_delta = pos
            row += r_delta
            col += col_delta
        print([row, col])
        return [row, col] == [0, 0]

# time complexity: O(N)
# space complexity: O(1)