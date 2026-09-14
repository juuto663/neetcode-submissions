class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            "}" : "{",
            "]" : "[",
            ")" : "(",
        }
        stack = []
        for symbol in s:
            if symbol in bracket_map:
                if stack and stack[-1] == bracket_map[symbol]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(symbol)
        if stack:
            return False
        return True
             