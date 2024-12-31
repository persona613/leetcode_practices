"""
143 ms runtime beats 92.38%
16.75 MB memory beats 6.28%
"""
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        # break at every index of s[l: r)
        def backtrack(l, r, seen):
            if l == r:
                return 0
            
            mx_cnt = 0
            curr = ""
            for i in range(l, r):
                curr += s[i]
                if curr not in seen:
                    seen.add(curr)
                    cnt = 1 + backtrack(i + 1, r, seen)
                    mx_cnt = max(mx_cnt, cnt)
                    seen.remove(curr)
            return mx_cnt

        return backtrack(0, len(s), set())                    