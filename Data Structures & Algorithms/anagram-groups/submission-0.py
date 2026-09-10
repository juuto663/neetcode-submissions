class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for let in word:
                index = ord(let) - ord('a') + 1
                count[index] += 1
            anagrams[tuple(count)].append(word)
        return anagrams.values()
        