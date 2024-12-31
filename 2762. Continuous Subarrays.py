"""
593 ms runtime beats 88.55%
27.49 MB memory beats 40.97%
"""
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        # sliding window
        # decreasing / increasing monotonic queue
        # queue store potencial break element's index
        deq = deque()
        inq = deque()
        ans = 0
        for r in range(n):
            curr = nums[r]
            if (
                deq and abs(curr - nums[deq[0]]) > 2 or 
                inq and abs(curr - nums[inq[0]]) > 2
            ):
                # window length
                ln = r - l
                # calculate subarray counts
                ans += (1 + ln) * ln // 2

                # shrink window to right most
                while deq and abs(curr - nums[deq[0]]) > 2:
                    l = max(l, deq.popleft() + 1)
                while inq and abs(curr - nums[inq[0]]) > 2:
                    l = max(l, inq.popleft() + 1)

                # pre minus overlap subarry
                k = r - l
                ans -= (1 + k) * k // 2

                # clear queue
                while deq and deq[0] < l:
                    deq.popleft()
                while inq and inq[0] < l:
                    inq.popleft()

            # update two queue
            while deq and nums[deq[-1]] <= curr:
                deq.pop()
            deq.append(r)
            while inq and nums[inq[-1]] >= curr:
                inq.pop()
            inq.append(r)

        ln = n - l
        ans += (1 + ln) * ln // 2
        return ans