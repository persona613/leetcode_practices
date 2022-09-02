
x = 10

if x < 0:
    print(False)
else:
    alist = list(str(x))
    rlist = alist[:]
    rlist.reverse()
    if alist == rlist:
        print(True)
    else:
        print(False)
    print(alist)
    print(rlist)