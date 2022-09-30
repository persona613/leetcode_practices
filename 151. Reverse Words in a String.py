'''
Runtime: 75 ms, faster than 16.05% of Python3 online submissions 
Memory Usage: 14 MB, less than 80.42% of Python3 online submissions 
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip(' ')
        s = s.split() # 默認刪除多重空格
        return ' '.join(s[::-1])