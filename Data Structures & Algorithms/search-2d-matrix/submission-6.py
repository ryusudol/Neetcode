class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            if matrix[i][n - 1] < target:
                continue
            
            l, r = 0, n - 1
            while l <= r:
                m = (l + r) // 2
                if matrix[i][m] == target:
                    return True
                elif matrix[i][m] < target:
                    l = m + 1
                else:
                    r = m - 1
            
            return False
            
        return False