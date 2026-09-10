class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, value in enumerate(nums):
            factor = target - value
            if factor in seen:
                return [seen[factor], index]
            seen[value] = index
        