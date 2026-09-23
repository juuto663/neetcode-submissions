class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            stone_1 = -heapq.heappop(heap)
            stone_2 = -heapq.heappop(heap)
            new_weight = -abs(stone_1 - stone_2)
            heapq.heappush(heap, new_weight)
        return -heap[0]