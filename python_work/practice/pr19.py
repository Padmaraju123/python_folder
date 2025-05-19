def app1(x):
    return int(x)






li = ["1","2","3","4"]

out = map(int,li)
for vv in out:
    print(vv)

print(list(map(app1,li)))

print(list(map(lambda x:int(x),li)))

li1 = [1,3,4]
li2 = ["1","3","4"]
print(list(map(lambda x,y : str(x)+y, li1,li2)))