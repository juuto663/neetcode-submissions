# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_width = 0
        self.dfs(root)
        return self.max_width

    def dfs(self, root):
        if not root:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        self.max_width = max(self.max_width, left + right)
        return max(left, right) + 1
