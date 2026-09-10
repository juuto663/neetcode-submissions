class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]

        for i in range (len(nums) - 1):
            prod = res[i] * nums[i]
            res.append(prod)
        
        carry = 1
        for i in range (len(nums) - 1, 0, -1):
            carry *= nums[i]
            res[i - 1] *= carry

        
        return res

# [1,2,4,6]
# [1,1,2,8]
# [48,24,12,8]

