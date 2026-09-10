from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """


        dict = {}
        for i in range (0, len(strs)):
            spelling = "".join(sorted(strs[i]))
            if spelling in dict.keys():
                dict[spelling].append(strs[i])
            else :
                dict[spelling] = [strs[i]]
        
        return dict.values()
        

