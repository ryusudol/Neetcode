# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque([root])

        while queue:
            cur = queue.popleft()
            if cur.val == subRoot.val and self.are_trees_same(cur, subRoot):
                return True
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        
        return False
    
    def are_trees_same(self, root: TreeNode, subRoot: TreeNode) -> bool:
        v1, v2 = [], []
        q1, q2 = deque([root]), deque([subRoot])

        while q1 and q2:
            cur1, cur2 = q1.popleft(), q2.popleft()

            v1.append(cur1.val)
            v2.append(cur2.val)

            if cur1.val != cur2.val:
                return False
            
            if cur1.left:
                q1.append(cur1.left)
            if cur1.right:
                q1.append(cur1.right)
            
            if cur2.left:
                q2.append(cur2.left)
            if cur2.right:
                q2.append(cur2.right)
        
        return not q1 and not q2 and v1 == v2