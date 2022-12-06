"""
Runtime: 2906 ms, faster than 15.16% of Python3 online submissions 
Memory Usage: 14.9 MB, less than 96.46% of Python3 online submissions
"""

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen = defaultdict(list)
        detect = ["0000"]
        start = 0
        tail = 0
        res = 0        
        
        if "0000" in deadends:
            return -1
        if "0000" == target:
            return 0
        
        while start <= tail:
            # check string numbers on current pace
            size = tail-start+1
            for _ in range(size):
                curr = detect[start]
                for i in range(4):
                    for increment in {1,-1}:
                        newd = (int(curr[i]) + increment) % 10
                        dis = [d for d in curr]
                        dis[i] = str(newd)
                        dis = "".join(dis)
                   
                        if dis in seen[dis[0]+dis[1]]:
                            continue                
                        if dis == target:
                            return res+1
                        if dis not in deadends:
                            detect.append(dis)
                            tail += 1
                        seen[dis[0]+dis[1]].append(dis)
            
                start += 1
            res += 1
        return -1
            
        