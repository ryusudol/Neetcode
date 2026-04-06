class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0] * cols for _ in range(rows)]
        for x in range(rows):
            total = 0
            for y in range(cols):
                total += matrix[x][y]
                self.prefix[x][y] = total

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for r in range(row1, row2 + 1):
            prefix_right = self.prefix[r][col2]
            prefix_left  = self.prefix[r][col1 - 1] if col1 > 0 else 0
            res += prefix_right - prefix_left
        return res