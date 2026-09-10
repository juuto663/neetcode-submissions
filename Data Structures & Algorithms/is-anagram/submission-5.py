class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mask = [0]*26

        if len(s) != len(t):
            return False
        
        for i in range (len(s)):
            mask[ord(s[i]) - ord('a')] +=1
            mask[ord(t[i]) - ord('a')] -= 1
        
        for i in range (len(mask)):
            if mask[i] != 0:
                return False
        return True