def FutFun(v, lss=None):
    if lss is None:
        lss = []
    lss.append(v)
    return lss


print(FutFun(1))
print(FutFun(2))
print(FutFun(3))