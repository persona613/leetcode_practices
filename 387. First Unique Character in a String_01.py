'''
Runtime: 159 ms, faster than 76.83% of Python3 online submissions 
Memory Usage: 14.1 MB, less than 58.94% of Python3 online submissions
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = []
        repeat = set()
        for c in s:
            if c in repeat:
                continue
            else:
                if c in ans:
                    ans.remove(c)
                    repeat.add(c)
                else:
                    ans.append(c)
        if len(ans) == 0:
            # print("Null")
            return -1
        else:
            # print(ans)
            return s.find(ans[0])