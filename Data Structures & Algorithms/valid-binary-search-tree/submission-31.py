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
            l_bound = max(l, curr.val)
            r_bound = min(r, curr.val)

            return (traverse(curr.left, l, l_bound) and
                    traverse(curr.right, r_bound, r))
        return traverse(root, -1001, 1001)


    # Left Root
        # Left [min(-inf, curr.val), curr.val]
        # Right [curr.val, root.val] 
    # Right Root
        # Left [root.val, curr.val]
        # Right [curr.val, Inf]