'''
Runtime: 40 ms, faster than 72.43% of Python3 online submissions 
Memory Usage: 16.69 MB, less than 95.48% of Python3 online submissions
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = dict()
        for i in range(len(s)):
            if s[i] not in dic and t[i] not in dic.values():
                dic[s[i]] = t[i]
            elif s[i] in dic and dic[s[i]] == t[i]:
                continue
            else:
                return False
        return True