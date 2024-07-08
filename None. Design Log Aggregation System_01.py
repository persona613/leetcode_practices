""" explore card: System Design
Submission Detail
136 / 164 test cases passed.
Status: Wrong Answer

Input:
["LogAggregator","pushLog","pushLog","pushLog","pushLog","pushLog","pushLog","pushLog","pushLog","pushLog","pushLog","pushLog","pushLog","getLogsFromMachine","getLogsOfService","search","search"]
[[3,3],[2322,1,1,"Machine 1 Service 1 Log 1"],[2312,1,1,"Machine 1 Service 1 Log 2"],[2352,1,1,"Machine 1 Service 1 Log 3"],[2298,1,1,"Machine 1 Service 1 Log 4"],[23221,1,2,"Machine 1 Service 2 Log 1"],[23121,1,2,"Machine 1 Service 2 Log 2"],[23222,2,2,"Machine 2 Service 2 Log 1"],[23122,2,2,"Machine 2 Service 2 Log 2"],[23521,1,2,"Machine 1 Service 2 Log 3"],[22981,1,2,"Machine 1 Service 2 Log 4"],[23522,2,2,"Machine 2 Service 2 Log 3"],[22982,2,2,"Machine 2 Service 2 Log 4"],[2],[2],[1,"Log 1"],[2,"Log 3"]]
Output:
[null,null,null,null,null,null,null,null,null,null,null,null,null,[23522,23122,22982,23222],[23521,23522,22981,22982,23121,23122,23221,23222],["Machine 1 Service 1 Log 1"],["Machine 1 Service 2 Log 3","Machine 2 Service 2 Log 3"]]
Expected:
[null,null,null,null,null,null,null,null,null,null,null,null,null,[23222,23122,23522,22982],[23221,23121,23222,23122,23521,22981,23522,22982],["Machine 1 Service 1 Log 1"],["Machine 1 Service 2 Log 3","Machine 2 Service 2 Log 3"]]
Submitted Code: 0 minutes ago
"""
class LogAggregator:

    def __init__(self, machines: int, services: int):
        self.ids = dict()
        self.machines = [set() for _ in range(machines)]
        self.services = [set() for _ in range(services)]

    def pushLog(self, logId: int, machineId: int, serviceId: int, message: str) -> None:
        self.ids[logId] = message
        self.machines[machineId].add(logId)
        self.services[serviceId].add(logId)

    def getLogsFromMachine(self, machineId: int) -> List[int]:
        return self.machines[machineId]

    def getLogsOfService(self, serviceId: int) -> List[int]:
        return self.services[serviceId]

    def search(self, serviceId: int, searchString: str) -> List[str]:
        res = []
        for d in self.services[serviceId]:
            if searchString in self.ids[d]:
                res.append(self.ids[d])
        return res


# Your LogAggregator object will be instantiated and called as such:
# obj = LogAggregator(machines, services)
# obj.pushLog(logId,machineId,serviceId,message)
# param_2 = obj.getLogsFromMachine(machineId)
# param_3 = obj.getLogsOfService(serviceId)
# param_4 = obj.search(serviceId,searchString)