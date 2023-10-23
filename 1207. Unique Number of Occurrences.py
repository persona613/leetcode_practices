"""
35 ms runtime beats 97.39%
16.44 MB memory beats 52.14%
"""
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        m = Counter(arr)
        seen = set()
        for v in m.values():
            if v in seen:
                return False
            seen.add(v)
        return True


        # m = Counter(arr)
        # return len(set(m.values())) == len(m.keys())