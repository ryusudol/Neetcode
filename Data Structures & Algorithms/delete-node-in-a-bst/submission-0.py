# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMinNode(self, node):
        cur = node
        while cur and cur.left:
            cur = cur.left
        return cur

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left: return root.right
            elif not root.right: return root.left
            else:
                min_node = self.findMinNode(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)
        
        return root