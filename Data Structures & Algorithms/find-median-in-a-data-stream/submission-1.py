class MedianFinder:

    def __init__(self):
        self.left_side = []
        self.right_side = []
        

    def addNum(self, num: int) -> None:
        # Both empty, pick left
        if not self.left_side and not self.right_side:
            heapq.heappush(self.left_side, -num)
            return

        # If it clearly belongs to the right, put it there else left
        if self.right_side and num > self.right_side[0]:
            heapq.heappush(self.right_side, num)
        else:
            heapq.heappush(self.left_side, -num)
        
        # Balance the two heaps
        while len(self.left_side) - len(self.right_side) > 1:
            num = -heapq.heappop(self.left_side)
            heapq.heappush(self.right_side, num)
        while len(self.right_side) - len(self.left_side) > 1:
            num = -heapq.heappop(self.right_side)
            heapq.heappush(self.left_side, num)


    def findMedian(self) -> float:
        if len(self.right_side) > len(self.left_side):
            return self.right_side[0]
        elif len(self.left_side) > len(self.right_side):
            return -self.left_side[0]
        else:
            return (self.right_side[0] + -self.left_side[0]) / 2
        
        