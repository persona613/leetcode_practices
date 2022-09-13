'''
Runtime: 77 ms, faster than 60.17% of Python3 online submissions for Final Value of Variable After Performing Operations.
Memory Usage: 13.9 MB, less than 12.49% of Python3 online submissions for Final Value of Variable After Performing Operations.
'''
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        acc = [1 if '+' in i else -1 for i in operations]
        return sum(acc)