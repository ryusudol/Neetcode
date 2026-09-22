# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pq, qq = deque([p]), deque([q])
        while pq and qq:
            p_cur, q_cur = pq.popleft(), qq.popleft()
            if not p_cur and not q_cur:
                continue
            if p_cur and q_cur and p_cur.val == q_cur.val:
                pq.append(p_cur.left if p_cur.left else None)
                pq.append(p_cur.right if p_cur.right else None)
                
                qq.append(q_cur.left if q_cur.left else None)
                qq.append(q_cur.right if q_cur.right else None)
            else:
                return False
        return not pq and not qq
