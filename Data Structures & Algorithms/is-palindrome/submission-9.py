class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while (l < r):
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                    continue
                else:
                    print(s[l], s[r])
                    return False
            elif s[l].isalnum() and not s[r].isalnum():
                r -= 1
            else:
                l += 1
        return True