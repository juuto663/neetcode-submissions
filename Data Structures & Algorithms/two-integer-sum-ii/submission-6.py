class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l <= r:
            potential_sum = numbers[l] + numbers[r]

            if target > potential_sum:
                l += 1
            elif target < potential_sum:
                r -= 1
            else:
                return [l + 1, r + 1]