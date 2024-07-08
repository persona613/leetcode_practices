"""
58 ms runtime beats 70.54%
16.75 MB memory beats 20.54%
"""
class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        # detect digits count
        d = 1
        curr = 2
        while curr < k:
            d += 1
            curr += 1 << d
            
        # minus one for 0-index
        index = k - (curr - (1 << d)) - 1
        # transfer to binary, pad zero to d-length
        index =f"{index:0{d}b}"

        # map: 0->4, 1->7
        ans = []
        for c in index:
            if c == "0":
                ans.append("4")
            else:
                ans.append("7")
        return "".join(ans)