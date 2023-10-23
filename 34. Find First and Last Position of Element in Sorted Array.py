"""
73 ms runtime beats 97.56%
17.8 MB memory beats 50.97%
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)-1
        def bs(l, r, side=None):
            while l <= r:
                m = (l+r)//2
                if nums[m] == target:
                    if not side:
                        return m
                    elif side == "r":
                        rs = bs(m+1, r, "r")
                        if rs < 0:
                            return m
                        else:
                            return rs
                    else:
                        ls = bs(l, m-1, "l")
                        if ls < 0:
                            return m
                        else:
                            return ls
                elif nums[m] < target:
                    l = m+1
                else:
                    r = m-1
            return -1

        ret = bs(0, n)
        if ret < 0:
            return [-1, -1]
        rs = bs(ret+1, n, "r")
        if rs == -1:
            rs = ret
        ls = bs(0, ret-1, "l")
        if ls == -1:
            ls = ret
        return [ls, rs]            