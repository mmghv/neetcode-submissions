class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        start, end = 0, (rows * cols) - 1
        while start <= end:
            mid = start + ((end - start) // 2)
            row, col = divmod(mid, cols)
            cell = matrix[row][col]
            if target == cell:
                return True
            elif target < cell:
                end = mid-1
            else:
                start = mid+1
        return False
            