# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -1000

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            res = max(res, l + node.val, r + node.val, l + r + node.val, node.val)
            return max(l, r, 0) + node.val

        dfs(root)
        return res