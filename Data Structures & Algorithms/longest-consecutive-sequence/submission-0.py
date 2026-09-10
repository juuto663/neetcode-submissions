class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = Counter(nums)
        global_max = 0


        local_count = 0
        for value in unique_nums:
            thread = value
            while (thread in unique_nums):
                local_count += 1
                if (thread + 1) in unique_nums:
                    thread += 1
                else:
                    global_max = max(global_max, local_count)
                    local_count = 0
                    break
        
        return global_max

