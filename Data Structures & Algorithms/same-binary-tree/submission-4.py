# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # p_to_visit = deque()
        # q_to_visit = deque()

        # if not p and not q:
        #     return True
        # if p and not q:
        #     return False
        # if q and not p:
        #     return False
        # p_to_visit.append(p)
        # q_to_visit.append(q)

        # while (p_to_visit and q_to_visit):
        #     p = p_to_visit[0]
        #     q = q_to_visit[0]
        #     if p and q:
        #         if p.val != q.val:
        #             return False
        #     elif not p and not q:
        #         p_to_visit.popleft()
        #         q_to_visit.popleft()
        #         continue
        #     else:
        #         return False
        #     p_to_visit.append(p.left)
        #     p_to_visit.append(p.right)
        #     q_to_visit.append(q.left)
        #     q_to_visit.append(q.right)
        #     p_to_visit.popleft()
        #     q_to_visit.popleft()
        # return True
        p_stack = []
        q_stack = []

        if not p and not q:
            return True
        if p and not q:
            return False
        if q and not p:
            return False

        def dfs(curr, stack):
            if not curr:
                stack.append(None)
                return None
            
            stack.append(curr)

            dfs(curr.left, stack)
            dfs(curr.right, stack)

            return stack
        p_stack = dfs(p, p_stack)
        q_stack = dfs(q, q_stack)
        
        if len(p_stack) != len(q_stack):
            return False
        
        for i in range(len(p_stack)):
            if p_stack[-1] and q_stack[-1]:
                if p_stack.pop().val != q_stack.pop().val:
                    return False
            elif not p_stack[-1] and not q_stack[-1]:
                p_stack.pop()
                q_stack.pop()
            else:
                return False
        return True
        
        

