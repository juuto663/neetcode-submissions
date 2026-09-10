# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.num_good = 0

        def dfs(curr, maximum):
            if not curr:
                return 0
            
            if curr.val >= maximum:
                maximum = curr.val
                self.num_good += 1

            dfs(curr.left, maximum)
            dfs(curr.right, maximum)
        
        dfs(root, root.val)
        return self.num_good          

