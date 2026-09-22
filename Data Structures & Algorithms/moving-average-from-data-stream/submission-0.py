class MovingAverage:

    def __init__(self, size: int):
        self.win_size = size
        self.running_sum = 0
        self.last_k = deque()

    def next(self, val: int) -> float:
        self.last_k.append(val)
        self.running_sum += val
        if len(self.last_k) <= self.win_size:
            return self.running_sum / len(self.last_k)
        else:
            num_to_remove = self.last_k.popleft()
            self.running_sum -= num_to_remove
            return self.running_sum / self.win_size

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
