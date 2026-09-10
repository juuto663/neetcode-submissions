# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes = 0
        def dfs(curr, max_val):
            if not curr:
                return 0
            print(curr.val, max_val)
            if curr.val >= max_val:
                max_val = curr.val
                self.good_nodes += 1
            dfs(curr.left, max_val)
            dfs(curr.right, max_val)

            return self.good_nodes
        return dfs(root, root.val)
