from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root

        # if not root:
        #     return None
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root