class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        heap = []

        for num, freq in freq_map.items():
            heapq.heappush(heap, (-freq, num))
        
        res = []
        for i in range(0, k):
            res.append(heapq.heappop(heap)[1])
        
        return res