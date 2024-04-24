"""
1136 ms runtime beats 30.42%
28.19 MB memory beats 99.15%
"""
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:

        def pick(tas):
            nonlocal n
            if tas == 0: return n
            cnt = i = 0
            j = 1
            while j < n:
                if price[j] - price[i] >= tas:
                    cnt += 1
                    i = j
                j += 1
            # print(f"tas={tas}, cnt={cnt + 1}")
            return cnt + 1 >= k

        n = len(price)
        price.sort()
        l = 0
        r = price[-1] - price[0]
        while l <= r:
            mid = (l + r) // 2
            # print(f"l={l},r={r},mid={mid},p={pick(mid)}")
            if pick(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r
