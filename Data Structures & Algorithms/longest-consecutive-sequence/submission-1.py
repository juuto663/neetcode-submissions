class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = Counter(nums)
        global_max = 0


        local_count = 0
        for value in unique_nums:
            thread = value
            while (unique_nums[thread]):
                local_count += 1
                if unique_nums[thread + 1]:
                    thread += 1
                else:
                    global_max = max(global_max, local_count)
                    local_count = 0
                    break
        
        return global_max

