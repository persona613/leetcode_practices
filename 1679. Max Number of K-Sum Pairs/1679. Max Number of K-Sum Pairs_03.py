'''Try: 用數對尋找次數'''

# nums = [1, 2, 3, 4]
# k = 5

nums = [3, 1, 3, 4, 3]
k = 6

pairs = []
count = 0
f = k // 2

for i in range(0, f):
    pairs.append([i+1, k-(i+1)])
print(pairs)

for p in pairs:
    print(p)
    if p[0] != p[1]:
        nc1 = nums.count(p[0])
        nc2 = nums.count(p[1])
        ms = min(nc1, nc2)
        # for i in range(ms):
        #     nums.remove(p[0])
        #     nums.remove(p[1])
        count = count + ms
    else:
        if nums.count(p[0]) >= 2:
            nc1 = nums.count(p[0])
            # for i in range(nc1//2*2):
            #     nums.remove(p[0])
            count = count + nc1 // 2

print(count)
#還是超過時間!!!
#取消刪除nums 超過記憶體空間






