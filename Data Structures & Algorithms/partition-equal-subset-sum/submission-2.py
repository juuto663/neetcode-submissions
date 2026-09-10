class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        dp = set()
        dp.add(0)

        target = sum(nums) / 2

        for i in range (len(nums) - 1, -1, -1):
            tmp = set()
            for t in dp:
                tmp.add(t + nums[i])
                tmp.add(t)
            dp = tmp

        return (True if target in dp else False)