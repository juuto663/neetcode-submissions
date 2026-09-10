# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_to_visit = deque()
        q_to_visit = deque()

        if not p and not q:
            return True
        if p and not q:
            return False
        if q and not p:
            return False
        p_to_visit.append(p)
        q_to_visit.append(q)

        while (p_to_visit and q_to_visit):
            p = p_to_visit[0]
            q = q_to_visit[0]
            if p and q:
                if p.val != q.val:
                    return False
            elif not p and not q:
                p_to_visit.popleft()
                q_to_visit.popleft()
                continue
            else:
                return False
            p_to_visit.append(p.left)
            p_to_visit.append(p.right)
            q_to_visit.append(q.left)
            q_to_visit.append(q.right)
            p_to_visit.popleft()
            q_to_visit.popleft()
        return True

