# app1

# dic1 = {} # dict()
#
# for i in range(3):
#     dic1[i] = input('enter the value of {} '.format(i))
#
# print(dic1)


# app2

dic2 = dict()
i = 0
while i<3:
    dic2[i] = input("Enter the value for key {} ".format(i))
    i+=1
print(dic2)


# app3

dic3 = dict(("name","raju"))
print((dic3))


dc1 = dict((input("Enter the key: "), [int(i) for i in input("Enter the value in list: ").split()]) for _ in range(3))

