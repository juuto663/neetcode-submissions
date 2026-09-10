class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    
        # test
        [-6,-3,-2,0,1,1,1,1,2,4,5,6,8]

        # sort it
        nums.sort()
        ret = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            search = -nums[i]
            while (l < r):
                attempt = nums[l] + nums[r]
                if attempt == search:
                    ret.append([nums[i], nums[l], nums[r]])
                    while (l < r) and nums[l] == nums[l + 1]:
                        l += 1
                    while (l < r) and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif attempt > search:
                    r -= 1
                else:
                    l += 1

        return ret