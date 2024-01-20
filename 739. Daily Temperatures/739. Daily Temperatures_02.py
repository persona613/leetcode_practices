"""
Time Limit Exceeded
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [len(temperatures)-1] * len(temperatures)
        dic = defaultdict(list)
        minn = 100
        maxx = 30
        find = False
        
        for i, t in enumerate(temperatures):
            minn = min(minn, t)
            maxx = max(maxx, t)
            dic[t].append(i)
            
        for t in range(minn, maxx+1, 1):
            while len(dic[t]):
                i = dic[t][-1]
                find = False
                warmer = t+1
                
                while warmer < 101:
                    for j in dic[warmer]:
                        if j > i:
                            ans[i] = min(ans[i], j-i)
                            find = True                        
                    warmer += 1
                    
                if find == False:
                    ans[i] = 0
                dic[t].pop()
        return ans
            
            