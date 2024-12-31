"""
210 ms runtime beats 37.61%
26.66 MB memory beats 62.01%
"""
class UndergroundSystem:

    def __init__(self):
        # check_in record: {id: [start_station, time]}
        self.ckin = dict()
        # {(start, end): [alltime, count]}
        self.alltime = defaultdict(lambda: [0] * 2)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ckin[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.ckin.pop(id)
        travel = (start_station, stationName)
        self.alltime[travel][0] += t - start_time
        self.alltime[travel][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        alltime, count = self.alltime[(startStation, endStation)]
        return alltime / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)