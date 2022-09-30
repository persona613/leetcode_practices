'''
Runtime: 58 ms, faster than 64.10% of Python3 online submissions
Memory Usage: 14.6 MB, less than 45.97% of Python3 online submissions
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(word):
            word = list(word)
            i = 0
            j = len(word)-1
            while i < j:
                word[i], word[j] = word[j], word[i]
                i += 1
                j -= 1
            word = ''.join(word)
            return word
        s = s.split()
        for i, val in enumerate(s):
            s[i] = reverse(val)
        return ' '.join(s)