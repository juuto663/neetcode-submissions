import heapq
class Solution:
    def isValid(self, s: str) -> bool:
        bracket_mapping = {
            ")": "(",
            "]": "[",
            "}": "{" 
        }
        stack = []
        for char in s:
            if not stack:
                if char in bracket_mapping:
                    return False
                stack.append(char)
                continue
            if stack[-1] == bracket_mapping.get(char, None):
                stack.pop()
                continue
            stack.append(char)
        
        if stack:
            return False
        return True
            
            
