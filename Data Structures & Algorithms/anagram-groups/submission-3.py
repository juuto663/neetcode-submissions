from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}

        for word in strs:
            mask = [0] * 26
            for char in word:
                mask[ord(char) - ord('a')] += 1
            if tuple(mask) in anagrams:    
                anagrams[tuple(mask)].append(word)
            else:
                anagrams[tuple(mask)] = [word]
        return anagrams.values()
