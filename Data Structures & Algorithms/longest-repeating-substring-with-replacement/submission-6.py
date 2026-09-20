class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if (n := len(s)) <= 1:
            return n
        
        l, r = 0, 1
        char_freq = {}
        char_freq[s[l]] = 1
        longest_str = 0


        while r < n:
            if not s[r] in char_freq:
                char_freq[s[r]] = 1
            else:
                char_freq[s[r]] += 1
            
            while sum(char_freq.values()) - max(char_freq.values()) > k:
                char_freq[s[l]] -= 1
                if char_freq[s[l]] == 0:
                    del char_freq[s[l]]
                l += 1
            
            r += 1
            longest_str = max(longest_str, r - l)
        
        return longest_str