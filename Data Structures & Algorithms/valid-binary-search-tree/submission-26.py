# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min_bound, max_bound = -1001, 1001

        def dfs(curr, min_bound, max_bound):
            if not curr:
                return True
            
            if not (min_bound < curr.val < max_bound):
                return False
            if curr.left and not (min_bound < curr.left.val < curr.val):
                return False
            if curr.right and not (curr.val < curr.right.val < max_bound):
                return False
            
            new_bound = max(min_bound, curr.val)

            return (dfs(curr.left, min_bound, new_bound) and
                    dfs(curr.right, new_bound, max_bound))
        
        return dfs(root, min_bound, max_bound)
