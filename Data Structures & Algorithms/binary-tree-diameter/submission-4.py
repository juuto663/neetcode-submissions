# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_width = 0
        def dfs(curr):
            if not curr:
                return 0
        
            left_count = dfs(curr.left)
            right_count = dfs(curr.right)
            self.max_width = max(self.max_width, left_count + right_count)
            return 1 + max(left_count, right_count)
        dfs(root)
        return self.max_width