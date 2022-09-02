'''Try: 用數對尋找次數'''

# nums = [1, 2, 3, 4]
# k = 5

nums = [3, 1, 3, 4, 3]
k = 6


count = 0
f = k // 2

for i in range(0, f):

    if i+1 == k-(i+1):
        if nums.count(i+1)//2 != 0:
            count = count + nums.count(i + 1) // 2
            for j in range(nums.count(i+1)//2*2):
                nums.remove(i+1)
    else:
        ms = min(nums.count(i+1), nums.count(k-(i+1)))
        if ms != 0:
            count = count + ms
            for j in range(ms):
                nums.remove(i+1)
                nums.remove(k-(i+1))


print(count)
#還是超過時間!!!
#取消刪除nums 超過記憶體空間
#還是時間超過!!!!






