class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            "}" : "{",
            "]" : "[",
            ")" : "(",
        }
        stack = []
        for symbol in s:
            if not stack and symbol in bracket_map:
                return False
            elif not stack or symbol not in bracket_map:
                stack.append(symbol)
                continue
            elif stack[-1] == bracket_map.get(symbol, None):
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True
             