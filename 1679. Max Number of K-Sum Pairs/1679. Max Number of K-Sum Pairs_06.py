'''Try: google'''

'''
Runtime: 867 ms, faster than 48.67% of Python3 online submissions for Max Number of K-Sum Pairs.
Memory Usage: 27.1 MB, less than 32.89% of Python3 online submissions for Max Number of K-Sum Pairs.
'''

from collections import Counter

nums = [1, 2, 3, 4]
k = 5

# nums = [3, 1, 3, 4, 3]
# k = 6

total = 0
ct = Counter(nums)
print(ct)

for n in ct:
    diff = k - n
    if n == diff:
        total = total + ct[n]//2
    if n < diff:
        total = total + min(ct[n], ct[diff])

print(total)


#還是超過時間!!!
#取消刪除nums 超過記憶體空間
#還是時間超過!!!!
#超過記憶體空間  0505:1850 - 0506:0100  6hrs 10min
#0506:0145 +45min





