'''
Runtime: 521 ms, faster than 32.6% of Python3 online submissions 
Memory Usage: 14.3 MB, less than 87.23% of Python3 online submissions
'''

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        bucket = {}
        for s1 in list1:
            for s2 in list2 :
                if s1 == s2:
                    sumi = list1.index(s1) + list2.index(s2)
                    if sumi in bucket:
                        bucket[sumi].append(s1)
                    else:
                        bucket[sumi] = [s1]
                    break
        anlist = sorted(bucket.keys())
        return bucket[anlist[0]]