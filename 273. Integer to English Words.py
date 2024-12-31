"""
40 ms runtime beats 33.87%
16.53 MB memory beats 75.27%
"""
class Solution:
    def numberToWords(self, num: int) -> str:
        dic = {0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000: "Thousand",
        1000000: "Million",
        1000000000: "Billion"
        }

        # ck: 3-digits-chunk index, from 0~3
        def helper(v, ck):
            if ck > 0 and v != 0:
                res.append(dic[(10 ** 3) ** ck])

            r = v % 100
            if r <= 20:
                res.append(dic[r])
            else:
                res.append(dic[r % 10])
                res.append(dic[(r//10) * 10])

            h = v // 100
            if h:
                # "Hundred" unit
                res.append(dic[100])
                res.append(dic[h])

        if num == 0:
            return "Zero"
        base = 10 ** 3
        ck = 0
        v = num
        res = []
        while v:
            r = v % base
            helper(r, ck)
            v //= base
            ck += 1
        res = [s for s in res if s != "Zero"]
        return " ".join(res[::-1])