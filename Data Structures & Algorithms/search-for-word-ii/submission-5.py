class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        rows, cols = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, cur):
            if not (
                0 <= r < rows and
                0 <= c < cols and
                (r, c) not in visited and
                board[r][c] in node.children
            ):
                return
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            cur += board[r][c]
            if node.is_word:
                res.add(cur)
            
            dfs(r + 1, c, node, cur)
            dfs(r, c + 1, node, cur)
            dfs(r - 1, c, node, cur)
            dfs(r, c - 1, node, cur)
            visited.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        
        return list(res)