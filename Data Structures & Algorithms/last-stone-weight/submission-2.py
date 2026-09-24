class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones_neg = [-stone for stone in stones]
        heapq.heapify(stones_neg)

        while len(stones_neg) > 1:
            stone_1 = heapq.heappop(stones_neg)
            stone_2 = heapq.heappop(stones_neg)
            new_stone_weight = abs(stone_1 - stone_2)
            heapq.heappush(stones_neg, -new_stone_weight)
        
        return -stones_neg[0]