"""
47 ms runtime beats 11.78%
16.71 MB memory beats 20.20%
"""
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for st in strings:
            key = []
            for i in range(1, len(st)):
                diff = ord(st[i]) - ord(st[i - 1])
                if diff < 0:
                    key.append(diff + 26)
                else:
                    key.append(diff)
            dic[tuple(key)].append(st)
            
        return [dic[k] for k in dic]