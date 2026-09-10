class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        stack = []

        #loop through every character
        for char in s:
            #if the stack is not empty, if char is in mapping, and the last element in stack is the correct value
            if (stack) and (char in mapping) and stack[-1] == mapping[char]:
                #Remove the last element added (it was succesfully closed, we don't need to consider it)
                stack.pop()
            else:
                #It must be an opener, so add it
                stack.append(char)
        #if the stack has values, return False (something wasn't closed) otherwise return True
        if stack:
            return False
        else:
            return True

