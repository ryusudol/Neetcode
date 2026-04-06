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
            l = max(dfs(node.left), 0)
            r = max(dfs(node.right), 0)
            res = max(res, l + r + node.val)
            return max(l, r) + node.val

        dfs(root)
        return res