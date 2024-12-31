"""
183 ms runtime beats 66.20%
19.20 MB memory beats 43.10%
"""
class BrowserHistory:

    def __init__(self, homepage: str):
        self.stk = [homepage]
        self.idx = 0

    def visit(self, url: str) -> None:
        while self.idx < len(self.stk) - 1:
            self.stk.pop()
        self.stk.append(url)
        self.idx += 1

    def back(self, steps: int) -> str:
        self.idx = max(0, self.idx - steps)
        return self.stk[self.idx]

    def forward(self, steps: int) -> str:
        self.idx = min(len(self.stk) - 1, self.idx + steps)
        return self.stk[self.idx]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)