from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        queue = deque([(sr, sc, start_color)])
        visited = set()
        while queue:
            c_row, c_col, c_color = queue.popleft()
            pos = (c_row, c_col)
            # print("pos", pos)
            if pos not in visited:
                image[c_row][c_col] = color
                visited.add(pos)
            
            deltas = [[1, 0], [-1, 0], [0, -1], [0, 1]]
            for delta in deltas:
                n_row = c_row + delta[0]
                n_col = c_col + delta[1]
                valid_row = 0 <= n_row < len(image)
                valid_col = 0 <= n_col < len(image[0])
                if (n_row, n_col) not in visited and valid_col and valid_row and image[n_row][n_col] == start_color:
                    # print("current", [c_row, c_col], "neighbor", [n_row, n_col])
                    queue.append((n_row, n_col, image[n_row][n_col]))

        return image

# time complexity: O(mn),m is the number of row, and n is the number of col of the image.
# space complexity:O(mn), number of items in the stack, worst case is all the item in the stack. 