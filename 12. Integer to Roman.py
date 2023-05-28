"""
50 ms runtime beats 64.44%
14 MB memory beats 23.19%
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        
        # trans digit to roman, code['I','V','X']
        def convert(d: int, code: List[str]) -> str:
            if d == 0: return ''
            if d >= 1 and d <= 3: return code[0]*d
            if d == 4: return code[0]+code[1]
            if d == 5: return code[1]
            if d >= 6 and d <= 8: return code[1]+code[0]*(d-5)
            if d == 9: return code[0]+code[2]

        lst = ['I','V','X','L','C','D','M']
        ans = ''
        if num > 999:
            q = num // 10**3
            num = num % 10**3
            ans += lst[-1]*q
        p = 2
        while num:
            q = num // 10**p
            num = num % 10**p
            ans += convert(q, lst[p*2:p*2+3])
            # print(codes)
            p -= 1
        return ans
