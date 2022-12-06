# Input: s = "()[]{}"
# Output: true

s = "()[]{}"
# s = "{{}[][[[]]]}"
# s = "{{}[][[[ ]]]}"


dic = {'(': 0, ')': 3, '[': 1, ']': 4, '{': 2, '}': 5}
stk = []
# s.split()
# print(s)
sl = list(s)
print(sl)
sl.pop()
print(sl)
# a = sl[-1:-3:-1]
# print(a)
del sl[-1:-3:-1]
print(sl)


