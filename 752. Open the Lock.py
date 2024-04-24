"""
Runtime: 242 ms, faster than 95.97% of Python3 online submissions 
Memory Usage: 18.29 MB, less than 23.87% of Python3 online submissions
"""
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
        if "0000" in deadends:
            return -1

        # next-slot
        ns = {"0": "1", "1": "2", "2": "3", "3": "4", "4": "5",
            "5": "6", "6": "7", "7": "8", "8": "9", "9": "0"}
        # pre-slot
        ps = {"0": "9", "1": "0", "2": "1", "3": "2", "4": "3",
            "5": "4", "6": "5", "7": "6", "8": "7", "9": "8"}
        deads = set()
        for dd in deadends:
            deads.add(tuple(dd))

        start = "0000"
        tg = list(target)
        q = deque([list(start)])
        seen = {tuple(start)}
        ans = 1
        while q:
            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                for i in range(4):
                    slot = curr[i]
                    adjs = [ps[slot], ns[slot]]
                    for adj in adjs:
                        curr[i] = adj
                        if curr == tg:
                            return ans
                        tcurr = tuple(curr)
                        if tcurr not in deads and tcurr not in seen:
                            seen.add(tcurr)
                            q.append(curr[:])
                    curr[i] = slot
            ans += 1
        return -1        