"""
123 ms runtime beats 46.93%
22.91 MB memory beats 19.30%
"""
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        if not words:
            return s

        trie = dict()
        END = "END"
        for word in words:
            curr = trie
            for c in word:
                curr = curr.setdefault(c, dict())
            curr[END] = True

        # scan out intervals
        intervals = deque()
        n = len(s)
        for i in range(n):
            if s[i] not in trie:
                continue
            curr = trie[s[i]]
            j = i + 1
            while j < n and s[j] in curr:
                curr = curr[s[j]]
                j += 1
            if END in curr:
                intervals.append([i, j])

        if not intervals:
            return s
        # print(intervals)

        # merge intervals and flatten
        merge = []
        curr = intervals.popleft()
        while intervals:
            nxt = intervals.popleft()
            # overlap to merge
            if curr[1] >= nxt[0]:
                # right most range
                curr[1] = max(curr[1], nxt[1])
            else:
                merge.extend(curr)
                curr = nxt
        merge.extend(curr)

        # insert tag
        res = []
        # merge interval array idx
        t = 0
        m = len(merge)
        tag0 = "<b>"
        tag1 = "</b>"
        for i in range(n):
            # insert time
            if t < m and i == merge[t]:
                if t % 2:
                    res.append(tag1)
                else:
                    res.append(tag0)
                t += 1
            res.append(s[i])
        if t < m:
            res.append(tag1)

        return "".join(res)