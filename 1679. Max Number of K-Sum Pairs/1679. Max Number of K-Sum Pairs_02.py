
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
        # print(p[0])
        while True:
            if p[0] in nums and p[1] in nums:
                nums.remove(p[0])
                nums.remove(p[1])
                count += 1
            else:
                break
    else:
        while True:
            if nums.count(p[0]) >= 2:
                nums.remove(p[0])
                nums.remove(p[0])
                count += 1
            else:
                break
print(count)
#還是超過時間!!!






