# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.are_same = True
        self.dfs(p, q)
        return self.are_same

    def dfs(self, p, q):
        if p and not q:
            self.are_same = False
        if q and not p:
            self.are_same = False
        if not p and not q:
            return None
        if not p:
            return None
        if not q:
            return None
        if p and q and p.val != q.val:
            self.are_same = False


        left = self.dfs(p.left, q.left)
        right = self.dfs(p.right, q.right)
        

