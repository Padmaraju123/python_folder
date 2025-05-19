# Position of maximum and minimum element in a list – Python

def max_min(lk):
    le = len(lk)

    for i in range(le):
        for j in range(i+1,le):
            if lk[i] > lk[j]:
                lk[i],lk[j] = lk[j], lk[i]

    max_ps = lk.index(lk[-1])
    min_ps = lk.index(lk[0])
    return max_ps,min_ps


# 2 4 0 1


list_num = [int(i) for i in input("Enter the number sequence: ").split()]
print(max_min(list_num))