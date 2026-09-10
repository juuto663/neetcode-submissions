class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. sort it O(nlogn)
        # 2. pick the first element
        # 3. use two pointers to find something that adds up to opposite of the first element
        # 4. If found, add to the list. If not (2 pointers are now equal, move onto the next element
        # 5. Keep a set of triplets so we can easily check duplicates (or just add everything to a set to dedup)

        nums.sort()
        ret = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            target = -nums[i]
            while (l < r):
                attempt = nums[l] + nums[r]
                if attempt == target:
                    ret.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif attempt > target:
                    r -= 1
                else:
                    l += 1
        
        return ret
