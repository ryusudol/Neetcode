class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(cur, seen):
            letter = word[len(cur)]
            cur += letter
            if len(cur) == len(word):
                return True
            for i in range(4):
                next_x, next_y = seen[-1][0] + delta[i][0], seen[-1][1] + delta[i][1]
                if 0 <= next_x < row and 0 <= next_y < col:
                    next_coord = (next_x, next_y)
                    print(cur, len(cur))
                    if next_coord not in seen and board[next_x][next_y] == word[len(cur)]:
                        seen.append(next_coord)
                        flag = dfs(cur, seen)
                        if flag:
                            return True
                        seen.remove(next_coord)
            cur = cur[:-1]
            return False

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    flag = dfs("", [(i, j)])
                    if flag:
                        return True
        return False