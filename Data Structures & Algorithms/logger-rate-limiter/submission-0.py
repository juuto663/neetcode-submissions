class Logger:

    def __init__(self):
        self.logs = defaultdict(int)


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if timestamp is None or message is None:
            return False
        elif message in self.logs:
            is_time = self.logs[message] <= timestamp
            if is_time:
                self.logs[message] = timestamp + 10
                return True
            else:
                return False
        else:
            self.logs[message] = timestamp + 10
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
