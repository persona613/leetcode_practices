'''
Runtime: 74 ms, faster than 64.69% of Python3 online submissions 
Memory Usage: 14.2 MB, less than 46.35% of Python3 online submissions
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic_st = {}
        dic_ts = {}
        for c1, c2 in zip(s, t):
            if c1 not in dic_st and c2 not in dic_ts:
                dic_st[c1] = c2
                dic_ts[c2] = c1
            elif (dic_st.get(c1) != c2) or (dic_ts.get(c2) != c1):
                return False
        return True