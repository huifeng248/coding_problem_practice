class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Note!!! 0 and 1 are STRING, need ""
        visited = set()
        count = 0
        for r in range(len(grid)):
            for col in range(len(grid[0])):
                if (r, col) not in visited:
                    if self.is_island(r, col, grid, visited):
                        count += 1
        
        return count 

    
    # def is_island(self, row, col, grid, visited):
    #     if row < 0 or row >= len(grid):
    #         return False
    #     if col < 0 or col >= len(grid[0]):
    #         return False
    #     if grid[row][col] == "0" or (row, col) in visited:
    #         return False
        
    #     visited.add((row, col))
    #     self.is_island(row+1, col, grid, visited)
    #     self.is_island(row-1, col, grid, visited)
    #     self.is_island(row, col+1, grid, visited)
    #     self.is_island(row, col-1, grid, visited)
    
    #     Note!!! this need reture True to be count !!!
    #     return True

# recursive time complexity: O(r*col) every node need to run once
# recursive space complexity: O(R*col) worst case recurssion stack have all the node


    def is_island(self, row, col, grid, visited):
        if grid[row][col] == "0" or (row, col) in visited:
            visited.add((row, col))
            return False

        stack = [(row, col)]
        while stack:
            current_row, current_col = stack.pop()

            if grid[current_row][current_col] == "1" and (current_row, current_col) not in visited: 
                visited.add((current_row, current_col))

                # Node!!!!: this need to go under/in the if condition
                deltas = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for delta in deltas:
                    new_row = current_row + delta[0]
                    new_col = current_col + delta[1]
                    valid_row = 0 <= new_row <len(grid)
                    valid_col = 0 <= new_col <len(grid[0])
                    if (new_row, new_col) not in visited and valid_row and valid_col and grid[new_row][new_col] == "1":
                        stack.append((new_row, new_col))
        
        return True

# time complexity: O(r*col) every node need to run once
# space complexity: O(R*col) worst case stack have all the node
