"""
Wrong Answer
64 / 65 testcases passed

Editorial
Input
["LogSystem","put","put","retrieve","retrieve", "retrieve"]
[[],[1,"2017:01:01:00:00:00"],[1,"2015:01:01:00:00:00"],["2015:01:01:00:00:00","2017:01:01:01:00:00","Year"],["2015:01:01:00:00:00","2015:01:01:00:00:01","Year"], ["2017:01:01:00:00:00","2017:01:01:00:00:01","Year"]]

Use Testcase
Output
[null,null,null,[1],[1],[1]]
Expected
[null,null,null,[1,1],[1],[1]]
"""
class LogSystem:

    def __init__(self):
        # yearid = {2000-2017: {timestamp: {id,...}}}
        self.yearid = defaultdict(lambda: defaultdict(set))
        # granularity to slice timestamp
        self.gran = {"Year":4, "Month":6, "Day":8, "Hour":10, 
                    "Minute":12, "Second":14}

    def put(self, id: int, timestamp: str) -> None:
        ts = "".join(timestamp.split(":"))
        curryear = int(ts[:4])
        self.yearid[curryear][ts].add(id)

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        k = self.gran[granularity]
        st = "".join(start.split(":"))[:k]
        nd = "".join(end.split(":"))[:k]
        res = set()
        styear = int(st[:4])
        ndyear = int(nd[:4])

        if styear == ndyear:
            logs = self.yearid[styear]
            for logtime in logs:
                t = logtime[:k]
                if st <= t <= nd:
                    res.update(logs[logtime])
        else:
            logs = self.yearid[styear]
            for logtime in logs:
                if st <= logtime[:k]:
                    res.update(logs[logtime])

            # find end year's ids
            logs = self.yearid[ndyear]
            for logtime in logs:
                if logtime[:k] <= nd:
                    res.update(logs[logtime])

            for iyear in range(styear + 1, ndyear):
                logs = self.yearid[iyear]
                for logtime in logs:
                    res.update(logs[logtime])
        return res



# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)