"""
52 ms runtime beats 19.67%
17.37 MB memory beats 41.60%
"""
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        m = Counter(arr)
        return len(set(m.values())) == len(m.values())


        # m = Counter(arr)
        # return len(set(m.values())) == len(m.keys())