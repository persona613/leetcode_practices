'''Try: 反向 從nums來分類'''

# nums = [1, 2, 3, 4]
# k = 5

nums = [3, 1, 3, 4, 3]
k = 6

dic = {}
total = 0
f = k // 2

if k % 2 == 0:
    if nums.count(f) != 0:
        total = total + nums.count(f)//2
    for i in range(nums.count(f)):
        nums.remove(f)

for i in range(0, f):
    dic[i] = {'num1': i+1, 'count1': 0, 'num2': k-(i+1), 'count2': 0}

for n in nums:
    for d in dic:
        if n == dic[d]['num1']:
            dic[d]['count1'] += 1
        if n == dic[d]['num2']:
            dic[d]['count2'] += 1

for d in dic:
    ms = min(dic[d]['count1'], dic[d]['count2'])
    total = total + ms


print(dic)


print(total)
#還是超過時間!!!
#取消刪除nums 超過記憶體空間
#還是時間超過!!!!
#超過記憶體空間  0505:1850 - 0506:0100  6hrs +10 m





