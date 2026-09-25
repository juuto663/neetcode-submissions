class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        heap = []

        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        ret = []
        for _ in range(k):
            freq, num = heapq.heappop(heap)
            ret.append(num)
        
        return ret