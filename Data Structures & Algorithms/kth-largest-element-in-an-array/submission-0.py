class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        
        k_largest = []
        for num in nums:
            heapq.heappush(k_largest, num)
            if len(k_largest) > k:
                heapq.heappop(k_largest)
        
        return k_largest[0]