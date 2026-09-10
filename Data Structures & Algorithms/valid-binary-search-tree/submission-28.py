# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr, min_bound, max_bound):
            if not curr:
                return True
            
            if not (min_bound < curr.val < max_bound):
                return False

            return (dfs(curr.left, min_bound, curr.val) and
                    dfs(curr.right, curr.val, max_bound))
        
        return dfs(root, -1001, 1001)
