@staticmethod
def binary_search(target: int, nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        midpoint = (l + r) // 2
        check_value = nums[midpoint]
        if check_value == target:
            return midpoint + 1
        elif check_value > target:
            r = midpoint - 1
        elif check_value < target:
            l = midpoint + 1
    return -1

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index, value in enumerate(numbers):
            search = target - value
            search_results = binary_search(target=search, nums=numbers[index + 1:])

            if search_results != -1:
                return [index + 1, index + 1 + search_results]
