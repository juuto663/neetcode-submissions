class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexer = {}

        for i in range (len(nums)):
            indexer[nums[i]] = i
        
        for i in range(len(nums)):
            second_num = target - nums[i]
            if second_num in indexer and indexer[second_num] != i:
                return [i, indexer[second_num]]
        
        return []