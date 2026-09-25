class Solution:
    def trap(self, height: List[int]) -> int:
        left_prefix = []
        local_max = 0

        for i in range(0, len(height)):
            left_prefix.append(local_max)
            local_max = max(local_max, height[i])

        right_prefix = [0] * len(height)
        local_max = 0

        for i in range(len(height) -1, -1, -1):
            right_prefix[i] = local_max
            local_max = max(local_max, height[i])

        valley_height = [min(x, y) for x, y in zip(left_prefix, right_prefix)]

        water = 0
        for i in range(len(height)):
            if valley_height[i] - height[i] > 0:
                water += valley_height[i] - height[i]
        
        return water

