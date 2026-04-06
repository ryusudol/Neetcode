from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        while queue:
            level_vals = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level_vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_vals:
                ans.append(level_vals)
        return ans