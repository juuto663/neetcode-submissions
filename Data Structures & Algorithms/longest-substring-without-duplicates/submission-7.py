class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      # abcabcbb
        if (n:= len(s)) <= 1:
            return n
        
        
        l, r = 0, 1
        longest_substr = 0
        seen = set()
        seen.add(s[l])

        while r < n:
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            r += 1
            longest_substr = max(longest_substr, r - l)
        
        return longest_substr
            