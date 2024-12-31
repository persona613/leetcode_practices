"""
107 ms runtime beats 48.30%
17.04 MB memory beats 45.10%
"""
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ppl = [(name, idx) for idx, name in enumerate(names)]
        ppl.sort(key = lambda x: heights[x[1]], reverse = True)
        return [p[0] for p in ppl]