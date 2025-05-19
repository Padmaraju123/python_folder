# # app1
# li0 = list() # or []
# for i in range(1,101):
#     li0.append(i)
# print(li0)
#
# # app2
# print([i for i in range(1,101)])
#
# #app3
# print(list(range(1,101)))
#
# #app4
# li1 = [i for i in range(1, 101)] * 2
# print(li1)
#
#app5
def convertion(v):
    return int(v)

li2 = list(map(convertion,range(1,101)))
print(li2)








