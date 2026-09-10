import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq_map = Counter(nums)
        for number, freq in freq_map.items():
            heapq.heappush(heap, (-freq, number))
        
        ret = []
        for i in range(k):
            freq, num = heapq.heappop(heap)
            ret.append(num)
        
        return ret
        