class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = Counter(s)
        t_dict = Counter(t)

        if (len(s_dict) != len(t_dict)):
            return False

        for char in s_dict:
            if s_dict[char] != t_dict[char]:
                return False
        return True

            