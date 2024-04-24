"""
1679 ms runtime beats 11.88%
24.40 MB memory beats 82.19%
"""
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        
        def testcost(k, n):
            if k == 0: return True
            q = deque()
            sm = 0
            for i in range(k):
                while q and chargeTimes[q[-1]] < chargeTimes[i]:
                    q.pop()
                q.append(i)
                sm += runningCosts[i]
            if chargeTimes[q[0]] + k * sm <= budget:
                return True

            for i in range(k, n):
                while q and chargeTimes[q[-1]] < chargeTimes[i]:
                    q.pop()
                q.append(i)

                if q[0] + k == i:
                    q.popleft()
                mxcharge = chargeTimes[q[0]]
                sm -= runningCosts[i - k]
                sm += runningCosts[i]
                if mxcharge + k * sm <= budget:
                    return True
            return False

        n = len(chargeTimes)
        l = 0
        r = len(chargeTimes) + 1
        while l < r:
            m = (l + r) // 2
            if testcost(m, n):
                if m + 1 == r:
                    return m
                else:
                    l = m
            else:
                r = m