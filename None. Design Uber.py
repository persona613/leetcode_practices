"""
2473 ms runtime beats None %
19.3 MB memory beats None %
"""
class Uber:

    def __init__(self):
        self.cabid = 1
        self.cabs = dict()
        # {customer id: cab id}
        self.trips = dict()

    def addCab(self, cabX: int, cabY: int) -> None:
        self.cabs[self.cabid] = (cabX, cabY)
        self.cabid += 1

    def startTrip(self, customerID: int, customerX: int, customerY: int) -> List[int]:
        if customerID in self.trips:
            return
        q = []
        for cab in self.cabs:
            cabX, cabY = self.cabs[cab]
            d = self.dist(customerX, customerY, cabX, cabY)
            # min heap
            heapq.heappush(q, (d, cabX, cabY, cab))
            
        if not q:
            return [-1, -1]
        d, cabX, cabY, cab = heapq.heappop(q)
        self.trips[customerID] = cab
        self.cabs.pop(cab)
        return [cabX, cabY]        

    def endTrip(self, customerID: int, customerX: int, customerY: int) -> None:
        if customerID not in self.trips:
            return
        cab = self.trips.pop(customerID)
        self.cabs[cab] = (customerX, customerY)

    def getNearestCabs(self, k: int, x: int, y: int) -> List[List[int]]:
        q = []
        for cab in self.cabs:
            cabX, cabY = self.cabs[cab]
            d = self.dist(x, y, cabX, cabY)
            # max heap
            if len(q) < k or d >= q[0][0]:
                heapq.heappush(q, (-d, -cabX, -cabY))
            if len(q) > k:
                heapq.heappop(q)
        res = []
        while q and len(res) < k:
            _, cabX, cabY = heapq.heappop(q)
            res.append((-cabX, -cabY))
        return sorted(res)
    
    def dist(self, x1, y1, x2, y2):
        return (x1 - x2) ** 2 + (y1 - y2) ** 2


# Your Uber object will be instantiated and called as such:
# obj = Uber()
# obj.addCab(cabX,cabY)
# param_2 = obj.startTrip(customerID,customerX,customerY)
# obj.endTrip(customerID,customerX,customerY)
# param_4 = obj.getNearestCabs(k,x,y)