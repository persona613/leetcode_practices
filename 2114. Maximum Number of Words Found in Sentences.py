'''
Runtime: 55 ms, faster than 73.04% of Python3 online submissions for Maximum Number of Words Found in Sentences.
Memory Usage: 13.9 MB, less than 42.51% of Python3 online submissions for Maximum Number of Words Found in Sentences.
'''
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        acc = []
        for i in sentences:
            i = i.split(' ')
            acc.append(len(i))
        return max(acc)