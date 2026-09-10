class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        num_freq = Counter(nums)
        print(num_freq)
        for num, freq in num_freq.items():
            # print(heap)
            # if len(heap) < k:
            #     print("adding")
            heapq.heappush(heap, (-freq, num))
            # elif -freq <= heap[0][0]:
            #     print("new king")
            #     heapq.heappush(heap, (-freq, num))
        
        ret = []
        for i in range (k):
            ret.append(heapq.heappop(heap)[1])

        return ret
