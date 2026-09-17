# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        nodes_to_visit = deque([root])
        levels = []
        while nodes_to_visit:
            sub_level = []
            for _ in range(len(nodes_to_visit)):
                node = nodes_to_visit.popleft()
                sub_level.append(node.val)
                if node.left:
                    nodes_to_visit.append(node.left)
                if node.right:
                    nodes_to_visit.append(node.right)
            levels.append(sub_level)
        
        return levels