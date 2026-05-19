class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_l, row_r = 0, len(matrix) - 1

        while row_l <= row_r:
            row_m = (row_l + row_r) // 2
            if target < matrix[row_m][0]:
                row_r = row_m - 1
            elif matrix[row_m][-1] < target:
                row_l = row_m + 1
            else:
                break
        
        col_l, col_r = 0, len(matrix[0]) - 1
        while col_l <= col_r:
            col_m = (col_l + col_r) // 2
            if target < matrix[row_m][col_m]:
                col_r = col_m - 1
            elif matrix[row_m][col_m] < target:
                col_l = col_m + 1
            else:
                return True
        return False