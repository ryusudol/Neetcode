class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, height):
            if not node:
                return (True, 0)
            is_balanced_l, height_l = dfs(node.left, height)
            is_balanced_r, height_r = dfs(node.right, height)
            return (is_balanced_l and is_balanced_r and abs(height_l - height_r) < 2, max(height_l, height_r) + 1)
        return dfs(root, 0)[0]