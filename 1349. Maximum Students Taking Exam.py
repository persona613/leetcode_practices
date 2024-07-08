"""
78 ms runtime beats 43.33%
16.64 MB memory beats 70.83%
"""
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        
        # row-index, pre row binary codes(1=has student)
        @lru_cache(None)
        def dp(i, pre):
            if i == m:
                return 0

            cnt = 0
            curr_seats = codes[i]
            
            # generate each possible arrange
            for p in range(2 ** n):
                p &= curr_seats
                # left_shift, right_shift of p
                lsh, rsh = p << 1, p >> 1

                # check both side seat's students
                if (p & lsh) or (p & rsh):
                    continue
                # check pre row students
                if (lsh & pre) or (rsh & pre):
                    continue

                # curr and next row students nums
                ccnt = p.bit_count()
                ncnt = dp(i + 1, p)
                if ccnt + ncnt > cnt:
                    cnt = ccnt + ncnt
            return cnt

        m = len(seats)
        n = len(seats[0])
        codes = []
        for i in range(m):
            bs = 0
            for j in range(n):
                if seats[i][j] == ".":
                    bs |= 1 << (n - 1 - j)
            codes.append(bs)
        return dp(0, 0)