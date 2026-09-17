class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left, right = 0, rows * cols -1
        while left <= right:
            m = (left + right) // 2
            row = m // cols
            col = m % cols

            if matrix[row][col] < target:
                left += 1

            elif matrix[row][col] > target:
                right -= 1

            else:
                return True
        return False