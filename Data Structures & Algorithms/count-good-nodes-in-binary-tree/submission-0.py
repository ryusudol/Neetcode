class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, max_val):
            nonlocal count
            if not node:
                return
            if max_val <= node.val:
                max_val = node.val
                count += 1
            dfs(node.left, max_val)
            dfs(node.right, max_val)
        dfs(root, -101)
        return count