import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        heap = []

        for num, freq in freq_map.items():
            heapq.heappush(heap, (-freq, num))         
        
        ret = []
        for i in range(k):
            freq, value = heapq.heappop(heap)
            ret.append(value)
        
        return ret
