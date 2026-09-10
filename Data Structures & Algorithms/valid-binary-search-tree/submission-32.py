# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(curr, l, r):
            if not curr:
                return True
            
            if not(l < curr.val < r):
                return False
            
            return (traverse(curr.left, l, curr.val) and
                    traverse(curr.right, curr.val, r))
        return traverse(root, -1001, 1001)