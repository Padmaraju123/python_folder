M = int(input())
a_set = set(map(int,input().split()))

N = int(input())
b_set = set(map(int, input().split()))


uni_val = list(a_set.union(b_set))
uni_val.sort()

[print(vv) for vv in uni_val]

