class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        
        res = []
        row, col = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, row-1, 0, col-1

        while top <= bottom and left <= right:
            # traverse top row from left to right
            for j in range(left, right+1, 1):
                res.append(matrix[top][j])
            top += 1

            # traverse right col from top to bottom
            for i in range(top, bottom+1, 1):
                res.append(matrix[i][right])
            right -= 1

            # traverse bottom row from right to left
            # Make sure we are now on a different row.
            if top <= bottom:
                for j in range(right, left-1, -1):
                    res.append(matrix[bottom][j])
            
            bottom -= 1

            # traverse left col from bottom to top
            # Make sure we are now on a different column.
            if left <= right:
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
            left += 1


        return res 

# time complexity: O(m&n) m is the row,n is the col of matrix, This is because we visit each element once.

# Space complexity: O(1). This is because we don't use other data structures. Remember that we don't include the output array in the space complexity.



        
