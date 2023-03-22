class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #thoughts: come from the borders, and mark the border with "O" to a third letters"E"; then change the       remaining "0" to "X", and change back the "E" to "O". 
        if not board or not board[0]:
            return 
        
        r, col = len(board), len(board[0])
        r_border = [[0, x] for x in range(col)] + [[r-1, x] for x in range(col)]
        col_border = [[y, 0] for y in range(r)] +[[y, col-1] for y in range(r)]
        
        borders = r_border + col_border
        # print("borders", borders)
        for pos in borders:
            row, column = pos[0], pos[1]
            self.mark_border(row, column, board)

        for row in range(r):
            for column in range(col):
                if board[row][column] == "O":
                    board[row][column] = "X"
                elif board[row][column] == "E":
                    board[row][column] = "O"
        return None

    def mark_border(self, row, col, board):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return 
        
        if board[row][col] != "O":
            return 
        board[row][col] = "E"

        self.mark_border(row+1, col, board)
        self.mark_border(row-1, col, board)
        self.mark_border(row, col+1, board)
        self.mark_border(row, col-1, board)

        return 

        
        