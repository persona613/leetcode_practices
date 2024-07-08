"""
121 ms runtime beats 8.80%
39.19 MB memory beats 5.25%
"""
class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        # path count, binary number
        def backtrack(i, bn):
            if i == end:
                if bn.bit_count() == 1:
                    return True
                return False

            # flip each bit
            for p in range(n):
                mask = 1 << p
                # detect every bit is 0 or 1
                if bn & mask == 0:
                    # flip 0 to 1
                    nxt = bn | mask
                else:
                    # flip 1 to 0
                    nxt = ~(~bn | mask)

                if nxt not in pool:
                    pool.add(nxt)
                    path.append(nxt)
                    ret = backtrack(i + 1, nxt)
                    if ret:
                        return True
                    pool.remove(nxt)
                    path.pop()
            return False

        path = [0]
        pool = {0}
        end = 2 ** n
        backtrack(1, 0)
        return path