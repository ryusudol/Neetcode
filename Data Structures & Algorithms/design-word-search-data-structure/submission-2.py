class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.word
            c = word[i]
            if c == '.':
                return any(dfs(child, i + 1) for child in node.children.values())
            return c in node.children and dfs(node.children[c], i + 1)
        return dfs(self.root, 0)