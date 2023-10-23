"""
1582 ms runtime beats 5.15%
45.3 MB memory beats 17.88%
"""
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.sort(key=lambda x:x[0])
        bloomed = sorted(flowers, key=lambda x:x[1])
        def st_bloom(lst, n, t):
            l = 0
            r = n
            while l <= r:
                m = (l+r)//2
                if lst[m][0] <= t:
                    if m+1<=n and lst[m+1][0]>t:
                        return m+1
                    else:
                        l = m+1
                else:
                    r = m-1
            if r<0: return 0
            return n+1

        def nd_bloom(lst, n, t):
            l = 0
            r = n
            while l <= r:
                m = (l+r)//2
                if lst[m][1] >= t:
                    r = m-1
                else:
                    if m+1<=n and lst[m+1][1]>=t:
                        return m+1
                    else:
                        l = m+1
            if r<0: return 0
            return n+1
        
        res = []
        n = len(flowers)-1
        for t in people:
            q = st_bloom(flowers, n, t)
            r = nd_bloom(bloomed, n, t)
            print(q, r)
            res.append(q-r)
        return res