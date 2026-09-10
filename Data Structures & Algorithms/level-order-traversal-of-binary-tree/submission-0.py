# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        nodes = deque([root])

        if not root:
            return []

        while nodes:
            len_nodes = len(nodes)
            for i in range(len_nodes):
                if nodes[i]:
                    if nodes[i].left:
                        nodes.append(nodes[i].left)
                    if nodes[i].right:
                        nodes.append(nodes[i].right)
                else:
                    nodes.append(None)
            sublist = []
            for i in range(len_nodes):
                if nodes[-1]:
                    sublist.append(nodes.popleft().val)
                else:
                    sublist.append(None)
            ret.append(sublist)
            
        return ret