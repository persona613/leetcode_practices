"""
569 ms runtime beats 36.84%
16.8 MB memory beats 77.76%
"""
class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        def cmp(wd1,wd2,n):
          for i in range(n):
            new = wd2[:i]+wd2[i+1:]
            if new == wd1:
              memo[wd2] = max(memo[wd1]+1, memo[wd2])
              return
        
        cd = defaultdict(list)
        for wd in words:
          cd[len(wd)].append(wd)
        # memo{str:length}
        memo = defaultdict(lambda :1)
        keylst = sorted(cd.keys())
        for i in range(len(keylst)-1):
          key = keylst[i]
          nxk = keylst[i+1]
          if key+1 == nxk:
            for wd1 in cd[key]:
              for wd2 in cd[nxk]:
                cmp(wd1,wd2,nxk)
        return max(memo.values()) if memo else 1