"""
438 ms runtime beats None %
26.5 MB memory beats None %
"""
class DCLoadBalancer:

    def __init__(self):
        # {id: Machine class}
        self.machines = dict()
        
        # {appid: machine_id}
        self.appfinder = dict()        
        
        # max heapq = [-machine_capacity, machine_id, statecode]
        self.q = list()
        
        # state code for machine capacity change
        self.counter = itertools.count()

    def addMachine(self, machineId: int, capacity: int) -> None:
        statecode = next(self.counter)
        new_machine = Machine(machineId, capacity, statecode)
        self.machines[machineId] = new_machine
        self.heappush_machine_state(new_machine)        

    def removeMachine(self, machineId: int) -> None:
        machine = self.machines.pop(machineId)
        
        for appid, loaduse in machine.apps.items():
            self.addApplication(appid, loaduse)

    def addApplication(self, appId: int, loadUse: int) -> int:
        while self.q:
            machine_capacity, machine_id, statecode = heapq.heappop(self.q)
            if machine_id not in self.machines:
                continue
                
            curr_machine = self.machines[machine_id]
            if curr_machine.statecode != statecode:
                continue
            if curr_machine.capacity >= loadUse:
                curr_machine.apps[appId] = loadUse
                curr_machine.capacity -= loadUse
                curr_machine.statecode = next(self.counter)
                self.appfinder[appId] = machine_id
                
                self.heappush_machine_state(curr_machine)
                return machine_id
            else:
                self.heappush_machine_state(curr_machine)
                break
        return -1

    
    def stopApplication(self, appId: int) -> None:
        if appId not in self.appfinder:
            return

        machine_id = self.appfinder.pop(appId)
        curr_machine = self.machines[machine_id]
        
        loaduse = curr_machine.apps.pop(appId)
        curr_machine.capacity += loaduse
        curr_machine.statecode = next(self.counter)
        
        self.heappush_machine_state(curr_machine)

        
    def getApplications(self, machineId: int) -> List[int]:
        return list(self.machines[machineId].apps.keys())[:10]
    
    
    def heappush_machine_state(self, curr_machine):
        if curr_machine.capacity <= 0:
            return
        machine_state = [-curr_machine.capacity,
                        curr_machine.id,
                        curr_machine.statecode]
        heapq.heappush(self.q, machine_state)        

class Machine:
    def __init__(self, machine_id, capacity, statecode):
        self.id = machine_id
        self.max_capacity = capacity
        self.capacity = capacity
        self.statecode = statecode
        
        # {appid: loaduse}
        self.apps = dict()


# Your DCLoadBalancer object will be instantiated and called as such:
# obj = DCLoadBalancer()
# obj.addMachine(machineId,capacity)
# obj.removeMachine(machineId)
# param_3 = obj.addApplication(appId,loadUse)
# obj.stopApplication(appId)
# param_5 = obj.getApplications(machineId)