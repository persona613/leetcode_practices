"""
517 ms runtime beats 58.22%
30.79 MB memory beats 68.49%
"""
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:

        def run(time):
            nonlocal b
            # search batteries's count 
            # that is >= time threshold for maintime charge
            for i in range(b):
                if batteries[i] < time:
                    break
            if i >= n:
                return True

            maintime = min(batteries[:i]) if i != 0 else inf

            # broken charge = sum(left batteries) / remaining computer
            left_time = sum(batteries[i:]) // (n - i)

            runtime = min(maintime, left_time)
            # print(f"t={runtime}, time={time}")
            return runtime >= time

        if n == 1:
            return sum(batteries)
        if n == len(batteries):
            return min(batteries)

        batteries.sort(reverse = True)
        b =  len(batteries)
        l = min(batteries[:n])
        r = sum(batteries) // n
        while l <= r:
            mid = (l + r) // 2
            # print(f"mid = {mid}, ret = {run(mid)}")
            if run(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r