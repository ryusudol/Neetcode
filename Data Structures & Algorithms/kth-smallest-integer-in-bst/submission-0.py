class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            visited.append(node.val)
            dfs(node.right)
        dfs(root)
        return visited[k - 1]