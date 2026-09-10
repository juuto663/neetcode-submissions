class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        stack = []

        for char in s:
            if (stack) and (char in mapping) and stack[-1] == mapping[char]:
                stack.pop()
            else:
                stack.append(char)
        if stack:
            return False
        else:
            return True
        #loop through characters in s
        #If it's in the mapping, and there is a top element of the stack and it is the value for the key
            #pop that element off the stack
        #Else
            #push to the stack
        #return true if the stack is empty, false otherwise
