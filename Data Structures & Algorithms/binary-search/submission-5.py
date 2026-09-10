class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        midpoint = (l + r) // 2

        while (l <= r):
            midpoint = (l + r) // 2
            if nums[midpoint] == target:
                return midpoint
            elif midpoint == l or midpoint == r:
                return -1
            elif nums[midpoint] < target:
                l = midpoint
            else:
                r = midpoint
        return -1