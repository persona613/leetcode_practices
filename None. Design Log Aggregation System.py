"""
44 ms runtime beats None %
21.5 MB memory beats None %
"""
class LogAggregator:

    def __init__(self, machines: int, services: int):
        self.ids = dict()
        self.machines = [list() for _ in range(machines)]
        self.services = [list() for _ in range(services)]

    def pushLog(self, logId: int, machineId: int, serviceId: int, message: str) -> None:
        self.ids[logId] = message
        self.machines[machineId].append(logId)
        self.services[serviceId].append(logId)

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