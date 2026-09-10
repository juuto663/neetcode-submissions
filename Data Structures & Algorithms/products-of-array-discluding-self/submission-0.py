class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_ltr = [nums[0]]
        for i in range(1, len(nums)):
            prefix_ltr.append(prefix_ltr[i-1] * nums[i])
        
        prefix_rtl = [None for num in nums]
        prefix_rtl[-1] = nums[-1]
        for i in range (len(nums) - 2, -1, -1):
            prefix_rtl[i] = prefix_rtl[i + 1] * nums[i]    

        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(prefix_rtl[i + 1])
            elif i == len(nums) - 1:
                res.append(prefix_ltr[i - 1])
            else:
                res.append(prefix_ltr[i - 1] * prefix_rtl[i + 1])

        return res
