"""
1053 ms runtime beats 16.17%
109.5 MB memory beats 5.50%
"""
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        shift = min(arr)
        maxn = max(arr)
        counts = [0]*(maxn-shift+1)
        for a in arr:
            counts[a-shift] += 1
        
        # starting indices
        sums = 0      
        for i, c in enumerate(counts):
            counts[i] = sums
            sums += c
        
        # new arr
        new = [0]*len(arr)
        for a in arr:
            new[counts[a-shift]] = a
            counts[a-shift] += 1
        
        # record distances of all pairs
        dp = defaultdict(list)
        for i in range(1, len(new)):
            dis = new[i]-new[i-1]
            dp[dis].append([new[i-1], new[i]])
            
        return dp[min(dp.keys())]
        