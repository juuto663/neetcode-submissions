# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Return empty list, if tree is None
        if not root:
            return []

        # Track of nodes to visit, and visible nodes
        to_visit = deque([root])
        visible = []

        # While there are nodes to visit 
        while to_visit:
            # Add the right most node
            visible.append(to_visit[-1].val)

            visit_len = len(to_visit)
            # Add children to the queue
            for i in range (visit_len): 
                node = to_visit.popleft()
                if node:
                    if node.left:
                        to_visit.append(node.left)
                    if node.right:
                        to_visit.append(node.right)
                else:
                    continue
        return visible