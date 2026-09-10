class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}
        for let in s:
            if let in s_hash:
                s_hash[let] += 1
            else:
                s_hash[let] = 1
        
        for let in t:
            if let in t_hash:
                t_hash[let] += 1
            else:
                t_hash[let] = 1
        
        if len(s_hash.keys()) != len(t_hash.keys()):
            return False

        for key in s_hash.keys():
            if key not in t_hash:
                return False
            if s_hash[key] != t_hash[key]:
                return False
        return True

