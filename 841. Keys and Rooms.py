'''
Runtime: 159 ms, faster than 25.97% of Python3 online submissions
Memory Usage: 15 MB, less than 14.14% of Python3 online submissions
'''

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # visited vrooms
        vr = set()
        
        # next room
        def next(i, rooms, vr):
            vr.add(i)
            if len(vr) == len(rooms):
                return True
            if len(rooms[i]) == 0:
                return 
            
            for k in rooms[i]:
                if k not in vr:
                    res = next(k, rooms, vr)
                    if res == True:
                        return True
        res = next(0, rooms, vr)
        if res == True:
            return True
        else:
            return False