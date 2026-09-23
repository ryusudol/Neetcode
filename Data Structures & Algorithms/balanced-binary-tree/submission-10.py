# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal res

            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            if abs(right - left) > 1:
                res = False

            return max(left, right) + 1
        
        dfs(root)

        return res