"""
38 ms runtime beats 38.70%
16.55 MB memory beats 44.21%
"""
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        cnt = Counter(s1.split())
        cnt += Counter(s2.split())
        return [word for word in cnt if cnt[word] == 1]