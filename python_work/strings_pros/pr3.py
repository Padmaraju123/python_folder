# Given a list like [1, 2, 3, 4], generate all possible pair combinations (without repetition).

lk = list(map(int,input("Enter the number sequence: ").split()))
le = len(lk)
out = []
for i in range(le):
    for j in lk[i+1:]:
        ot =[lk[i],j]
        if (ot not in out) and (ot[::-1] not in out):
            out.append(ot)
print(out)


