d1 = {"name":"raju","age":27}
print(d1,type(d1),id(d1))

d2 = dict(name="raju",age=27)
print(d2)

d3 = dict([["name","raju"],["age",27]])
print(d3)

d4 = dict([("name","raju"),("age",27)])
print(d4)

d5 = dict((("name","raju"),("age",27)))
print(d5)

d6 = dict((["name","raju"],["age",27]))
print(d6)


keys = ['name', 'age']
values = ['Alice', 30]
d7 = dict(zip(keys, values))
print(d7)

keys = ('name', 'age')
values = ('Alice', 30)
d8 = dict(zip(keys, values))
print(d8)


# dictionary comprehension
d9 = {x:x*2 for x in range(3)}
print(d9)

d10 = dict()
for key,val in zip(keys,values):
    d10[key] = val

print("The dictionary 10 is {}".format(d10))








