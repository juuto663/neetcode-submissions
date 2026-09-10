class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # [1, 2, 8, 48] -->
        # [48, 48,24,6] <--
        # [48,24,12, 8]
    
        left_prefix_sum = [nums[0]]
        for x in range(1, len(nums)):
            left_prefix_sum.append(left_prefix_sum[x - 1] * nums[x])
    
        nums.reverse()
        right_prefix_sum = [nums[0]]
        for x in range(1, len(nums)):
            right_prefix_sum.append(right_prefix_sum[x - 1] * nums[x])
        right_prefix_sum.reverse()
        nums.reverse()
        
        ret = []
        for i in range(len(nums)):
            if i == 0:
                print(right_prefix_sum, i)
                ret.append(right_prefix_sum[i + 1])
            elif i == len(nums) - 1:
                ret.append(left_prefix_sum[i - 1])
            else:
                ret.append(left_prefix_sum[i - 1] * right_prefix_sum[i + 1])

        return ret
            