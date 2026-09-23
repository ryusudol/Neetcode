# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node: TreeNode, cur_max: int) -> int:
            nonlocal res

            if not node:
                return 0
            
            if cur_max <= node.val:
                res += 1
                cur_max = node.val
            
            left = dfs(node.left, cur_max)
            right = dfs(node.right, cur_max)

            return left + right
        
        dfs(root, float('-inf'))

        return res