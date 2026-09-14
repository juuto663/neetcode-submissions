class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            search_index = (l + r) // 2
            if nums[search_index] < target:
                l = search_index + 1
            elif nums[search_index] > target:
                r = search_index - 1
            else:
                return search_index
        return -1