class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # AAABABB
        if (s_length:= len(s)) <= 1:
            return s_length

        
        longest_str = 0
        l, r = 0, 1
        chars = defaultdict(int)
        chars[s[l]] += 1

        while r < s_length:
            chars[s[r]] += 1
            while (sum(chars.values()) - max(chars.values()) > k):
                chars[s[l]] -= 1
                if chars[s[l]] == 0:
                    del chars[s[l]]
                l += 1
            r += 1
            longest_str = max(longest_str, r - l)
            
            
        
        return longest_str

