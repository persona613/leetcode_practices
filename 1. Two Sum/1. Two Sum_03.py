import typing

'''
參考八號黃俊偉同學的coding
86ms 63.15% Time, 15.1MB 50.08% Space
'''

nums = [2, 7, 11, 15]
target = 9

# nums = [3, 2, 4]
# target = 6

# nums = [3, 3]
# target = 6

# nums = [2, 5, 6, 8, 10, 11, 12, 13, 15]
# target = 24


done: typing.Dict[int, int] = {}
for index, value in enumerate(nums):
    rest: int = target - value
    if rest in done:
        ans = [done[rest], index]
    done[value] = index

print(ans)