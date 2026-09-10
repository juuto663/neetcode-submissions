class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            mask = [0] * 26
            for char in string:
                mask[ord(char) - ord('a')] += 1
            
            mask = tuple(mask)

            if mask in anagrams:
                anagrams[mask].append(string)
            else:
                anagrams[mask] = [string]
        
        return anagrams.values()
            