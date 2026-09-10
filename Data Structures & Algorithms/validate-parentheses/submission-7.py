class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack = []

        if s[0] in mapping:
            return False

        for char in s:
            if char in mapping:
                if (stack) and (mapping[char] == stack[-1]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        if (stack):
            return False
        else:
            return True