"""
38 ms runtime beats 36.65%
16.68 MB memory beats 13.04%
"""
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:

        def helper(arr1, arr2):
            n = min(len(arr1), len(arr2))
            prefix = surfix = 0
            for a, b in zip(arr1, arr2):
                if a == b:
                    prefix += 1
                else:
                    break
            if prefix == n:
                return True

            for a, b in zip(arr1[::-1], arr2[::-1]):
                if a == b:
                    surfix += 1
                else:
                    break
            if surfix == n:
                return True

            if prefix == 0 or surfix == 0:
                return False
            return helper(arr1[prefix: -surfix], arr2[prefix: -surfix])

        arr1 = sentence1.split()
        arr2 = sentence2.split()
        return helper(arr1, arr2)