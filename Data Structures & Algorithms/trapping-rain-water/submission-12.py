class Solution:
    def trap(self, height: List[int]) -> int:

        biggest_from_left = 0
        for i, v in enumerate(height):
            biggest_from_left = max(biggest_from_left, v)
            height[i] = max(biggest_from_left - height[i], 0)

        biggest_from_right = 0
        for i in range(len(height) - 1, -1, -1):
            biggest_from_right = max(biggest_from_right, (biggest_from_left - height[i]))
            height[i] = height[i] - (biggest_from_left - biggest_from_right)

        max_sum = 0
        for num in height:
            max_sum += num
        return max_sum

        
            