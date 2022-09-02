nums = [1, 3, 5, 6]
target = 7

t = len(nums)
i = 0
find = False

while i < t and find == False:
    if target == nums[i]:
        print(i)
        find = True
    elif target < nums[i]:
        print(i)
        find = True
    elif target > nums[i]:
        pass
    i += 1
if i == t:
    print(i)

