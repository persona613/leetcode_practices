# Runtime: 25 ms, faster than 98.99% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.9 MB, less than 51.33% of Python3 online submissions for Longest Common Prefix.

# 參考使用 &=

# strs = ["flow", "flow", "flow"]
# strs = ["flower", "flow", "flight"]
# strs = ["flower", "flow", "flight"]
strs = ["racecls", "racecar", "raceca"]




lens = [len(strs[i]) for i in range(len(strs))]  # list[字串長度]
ms = min(lens)  # 字串最小長度

p = True  # 控制迴圈開關
idx = 0   # 字串idx
while idx < ms and p:
    i = 0
    while i < len(strs) - 1:
        if strs[i][idx] == strs[i+1][idx]:
            pass
        else:
            p = False
            break
        i += 1
    idx += 1

#所有字串皆相同
if p is True:
    idx = ms
    print(strs[0][:ms])
else:
    #所有字串皆不相同
    if idx == 1:
        print('""')
    #部分字串相同
    else:
        idx -= 2
        print(strs[0][:idx+1])


