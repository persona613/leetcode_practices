"""
65 ms runtime beats 56.36%
16.4 MB memory beats 22.39%
"""
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # calculate consective 1's numbers from list[-2] till 0 appear
        # if 1's nums is odd, return False, else True
        cnt = 0 # store 1's nums
        for i in range(-2, -len(bits)-1, -1):
            if bits[i] == 0:
                break
            cnt += 1
        return cnt % 2 == 0