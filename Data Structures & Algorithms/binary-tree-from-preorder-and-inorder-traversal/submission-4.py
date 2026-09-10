# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def tree_builder(preorder, inorder):
            if not preorder or not inorder:
                return None
            if len(inorder) == 1 or len(preorder) == 1:
                print("returning ", inorder[0])
                return TreeNode(inorder[0], None, None)

            root = preorder[0]
            inorder_pivot = None
            for i in range(len(inorder)):
                if inorder[i] == root:
                    inorder_pivot = i + 1
                    break

            left = tree_builder(preorder[1:inorder_pivot], inorder[0:inorder_pivot - 1])
            right = tree_builder(preorder[inorder_pivot:], inorder[inorder_pivot:])
            
            return TreeNode(root, left, right)
        return tree_builder(preorder, inorder)