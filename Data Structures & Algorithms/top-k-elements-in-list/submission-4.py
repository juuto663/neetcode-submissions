class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the number of elements in nums
        num_elems = {}
        bucket = [[] for i in range (len(nums) + 1)]
        for i in range(len(nums)):
            if nums[i] in num_elems:
                num_elems[nums[i]] += 1
            else:
                num_elems[nums[i]] = 1
        
        for number, count in num_elems.items():
            bucket[count].append(number)

        ret = []
        for i in range (len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                ret.append(num)
                if (len(ret) == k):
                    return ret

        