"""
257 ms runtime beats 98.61%
23.49 MB memory beats 26.39%
"""
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        tsum = sum(arr)
        if tsum % 3:
            return False
        k = tsum // 3
        n = len(arr)
        ls = rs = 0
        for i in range(n-2):
            ls += arr[i]
            if ls == k:
                break
        else:
            return False
        for j in range(n-1, i+1, -1):
            rs += arr[j]
            if rs == k:
                break
        else:
            return False
        return True