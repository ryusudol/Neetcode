# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_depth = 1
        queue = deque([(1, root)])

        while queue:
            cur_depth, cur_node = queue.popleft()
            max_depth = max(max_depth, cur_depth)
            if cur_node.left:
                queue.append((cur_depth + 1, cur_node.left))
            if cur_node.right:
                queue.append((cur_depth + 1, cur_node.right))
        
        return max_depth