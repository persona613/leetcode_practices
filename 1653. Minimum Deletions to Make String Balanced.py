"""
542 ms runtime beats 30.67%
22.81 MB memory beats 10%
"""
class Solution:
    def minimumDeletions(self, s: str) -> int:
        # Bs: prefix sum of b_count before curr i
        # As: surfix sum of a_count after curr i
        # cost = Bs[i - 1] + Ax[i + 1]
        # pad zero to simplify cost = Bs[i] + As[i]
        Bs = [0]
        for c in s:
            if c == "b":
                Bs.append(Bs[-1] + 1)
            else:
                Bs.append(Bs[-1])
        As = [0]
        for c in reversed(s):
            if c == "a":
                As.append(As[-1] + 1)
            else:
                As.append(As[-1])

        # min(sum(pair) for pair in zip(As[::-1], Bs))
        return min(map(sum, zip(As[::-1], Bs)))