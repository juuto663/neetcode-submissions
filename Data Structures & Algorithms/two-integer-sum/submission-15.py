class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indicies = {}
        for i in range (len(nums)):
            indicies[nums[i]] = i
        
        for i in range (len(nums)):
            search = target - nums[i]
            if search in indicies:
                if indicies[search] != i:
                    return [i, indicies[search]]
            
        
        
        


        