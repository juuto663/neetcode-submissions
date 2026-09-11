class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, v in enumerate(nums):
            search = target - v
            if search in seen:
                return [seen[search], i]
            seen[v] = i
        