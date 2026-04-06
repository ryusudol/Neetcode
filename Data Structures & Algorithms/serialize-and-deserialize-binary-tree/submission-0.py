# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        queue = deque([root])
        visited = []
        while queue:
            cur = queue.popleft()
            if cur:
                visited.append(str(cur.val))
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                visited.append("N")
        return ",".join(visited)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        if data[0] == "N":
            return None
        root = TreeNode(int(data[0]))
        queue = deque([root])
        idx = 1
        while queue:
            cur = queue.popleft()
            if data[idx] != "N":
                cur.left = TreeNode(int(data[idx]))
                queue.append(cur.left)
            idx += 1
            if data[idx] != "N":
                cur.right = TreeNode(int(data[idx]))
                queue.append(cur.right)
            idx += 1
        return root