class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root