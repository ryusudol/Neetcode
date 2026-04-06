from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True
            elif (not p or not q) or p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if isSameTree(node, subRoot):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False