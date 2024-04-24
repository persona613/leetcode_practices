"""
40 ms runtime beats 51.82%
16 MB memory beats 100%
"""
class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace("6", "9", 1))

        # lst = list(str(num))
        # for i in range(len(lst)):
        #     if lst[i] == "6":
        #         lst[i] = "9"
        #         return int("".join(lst))
        # return num