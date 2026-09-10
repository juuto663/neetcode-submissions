# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        count_left = 1
        count_right = 1
        
        if root.left:
            count_left += self.maxDepth(root.left)
        if root.right:
            count_right += self.maxDepth(root.right)

        return max(count_left, count_right)