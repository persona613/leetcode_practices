# Runtime: 57 ms, faster than 67.53% of Python3 online submissions for Roman to Integer.
# Memory Usage: 13.9 MB, less than 78.29% of Python3 online submissions for Roman to Integer.


'''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

'III'       3
'LVIII'     58
'MCMXCIV'   1994
'''

# s = 'III'
# s = 'LVIII'
# s = 'MCMXCIV'
s = 'IV'

cha = 'IVXLCDM'
val1 = [1, 5, 10, 50, 100, 500, 1000]
dic1 = {}
sums = 0
pre = 0

for idx, c in enumerate(cha):
    dic1[c] = val1[idx]

for rom in s[::-1]:
    if dic1[rom] >= pre:
        sums += dic1[rom]
    else:
        sums -= dic1[rom]
    pre = dic1[rom]

print(sums)
