class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        k_closet = []

        for x, y in points:
            dist = math.sqrt((x - 0)**2 + (y - 0)**2)
            heapq.heappush(k_closet, (-dist, x, y))
            if len(k_closet) > k:
                heapq.heappop(k_closet)
            
        ret = []
        for _ in range(k):
            dist, x, y = heapq.heappop(k_closet)
            ret.append([x, y])
        
        return ret