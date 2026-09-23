# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node: TreeNode, cur_max: int) -> None:
            nonlocal res

            if not node:
                return
            
            if cur_max <= node.val:
                res += 1
                cur_max = node.val
            
            dfs(node.left, cur_max)
            dfs(node.right, cur_max)
        
        dfs(root, float('-inf'))

        return res