# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]) -> List[int | bool]:
            if not root:
                return [True, float('inf'), float('-inf')]
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            is_valid = left[0] and right[0] and left[2] < root.val < right[1]
            minimum = root.val if left[1] == float('inf') else left[1]
            maximum = root.val if right[2] == float('-inf') else right[2]

            return [is_valid, minimum, maximum]
        
        return dfs(root)[0]