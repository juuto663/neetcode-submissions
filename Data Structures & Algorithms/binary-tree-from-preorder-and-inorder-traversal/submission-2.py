# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        pre_dict = {k: v for v, k in enumerate(preorder)}
        in_dict = {k: v for v, k in enumerate(inorder)}

        #Preorder [1,2,3,4], Inorder [2,1,3,4]
        def tree_builder(preorder, inorder):
            print("lists: ", preorder, inorder)
            if not preorder or not inorder:
                return None
            if len(inorder) == 1 or len(preorder) == 1:
                print("returning ", inorder[0])
                return TreeNode(inorder[0], None, None)

            #determine root

            root = preorder[0]
            inorder_pivot = None
            for i in range(len(inorder)):
                if inorder[i] == root:
                    inorder_pivot = i + 1
                    break
            print("root/pivot: ", root, inorder_pivot)

            left = tree_builder(preorder[1:inorder_pivot], inorder[0:inorder_pivot - 1])
            right = tree_builder(preorder[inorder_pivot:], inorder[inorder_pivot:])

            print("nodes: ", left, right)

            # if left and left.val == root:
            #     return None
            # if right and right.val == root:
            #     return None
            
            return TreeNode(root, left, right)
        return tree_builder(preorder, inorder)