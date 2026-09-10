class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, v in enumerate(nums):
            search_for = target - v
            if search_for in seen.keys():
                return [seen[search_for], i]
            seen[v] = i