# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        queue = deque([(float('-inf'), root)])
        
        while queue:
            cur_max, cur_node = queue.popleft()
            if cur_max <= cur_node.val:
                res += 1
                cur_max = cur_node.val
            
            if cur_node.left:
                queue.append((cur_max, cur_node.left))
            if cur_node.right:
                queue.append((cur_max, cur_node.right))
        
        return res