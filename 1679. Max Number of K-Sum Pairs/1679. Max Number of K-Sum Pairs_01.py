
nums = [1, 2, 3, 4]
k = 5

nums = [3, 1, 3, 4, 3]
k = 6

prenums = []
i = 0
for n in nums:
    diff = k - n
    if diff in prenums:
        prenums.remove(diff)
        i += 1
    else:
        prenums.append(n)

print(i)