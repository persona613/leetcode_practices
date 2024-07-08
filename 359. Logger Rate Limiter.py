"""
113 ms runtime beats 86.93%
22.40 MB memory beats 83.31%
"""
class Logger:

    def __init__(self):
        self.log = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.log:
            ret = True
            self.log[message] = timestamp + 10
        else:
            if timestamp < self.log[message]:
                ret = False
            else:
                ret = True
                self.log[message] = timestamp + 10
        return ret


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)