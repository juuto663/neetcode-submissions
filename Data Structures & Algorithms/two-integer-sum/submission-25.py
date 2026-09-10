class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for index, num in enumerate(nums):
            search = target - num
            if search in seen:
                return [seen[search], index]
            seen[num] = index
            