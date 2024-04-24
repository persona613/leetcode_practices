"""
32 ms runtime beats 90.37%
16.70 MB memory beats 20.59%
"""
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        arr = sorted(clips)
        n = len(arr)
        ans = rlimit = 0
        i = 0
        # res = []
        while i < n:
            if arr[i][0] <= rlimit:
                # res.append(arr[i])
                tmp_r = arr[i][1]
                j = i + 1
                while j < n:
                    if arr[j][0] <= rlimit:
                        if arr[j][1] > tmp_r:
                            tmp_r = arr[j][1]
                            # res.pop()
                            # res.append(arr[j])
                        j += 1
                    else:
                        break
                ans += 1
                rlimit = tmp_r
                if rlimit >= time:
                    break
                i = j
            else:
                i += 1
        # print(res)
        return ans if rlimit >= time else -1