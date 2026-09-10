class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            mask = [0] * 26
            for letter in word:
                mask[ord(letter) - ord('a')] += 1
            
            mask = tuple(mask)

            if mask in anagrams:
                anagrams[mask].append(word)
            else:
                anagrams[mask] = [word]
        
        return anagrams.values()