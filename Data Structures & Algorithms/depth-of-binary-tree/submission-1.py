from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_depth = 0
        queue = deque([(1, root)])
        while queue:
            depth, node = queue.popleft()
            max_depth = max(max_depth, depth)
            if node.left:
                queue.append((depth + 1, node.left))
            if node.right:
                queue.append((depth + 1, node.right))
        return max_depth

        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))