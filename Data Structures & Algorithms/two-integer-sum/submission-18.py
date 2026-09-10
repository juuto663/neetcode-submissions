class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        seen = {}

        for k, v in enumerate(nums):
            factor = target - v
            if factor in seen:
                return [seen[factor], k]
            else:
                seen[v] = k
            
