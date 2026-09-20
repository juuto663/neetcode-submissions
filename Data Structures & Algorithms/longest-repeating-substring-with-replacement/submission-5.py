class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # AAABABB, k=1 -> 5 but mine says 7
        if (n := len(s)) <= 1:
            return n
        
        freq_map = {}
        l, r = 0, 1
        freq_map[s[l]] = 1
        longest_str = 1 


        while r < n: 
            if not s[r] in freq_map:
                freq_map[s[r]] = 1
            else:
                freq_map[s[r]] += 1

            # While there are too many chars, or there are too many non-dominant chars
            while sum(freq_map.values()) - max(freq_map.values()) > k:
                freq_map[s[l]] -= 1
                if freq_map[s[l]] == 0:
                    del freq_map[s[l]]
                l += 1

            r += 1
            longest_str = max(longest_str, r - l)
            

        return longest_str