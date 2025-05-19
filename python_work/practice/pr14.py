# Convert a dictionary’s keys or values into a list.


class Working14:

    def __init__(self,ddk):
        self.ddk = ddk

    def app1(self):
        print(list(self.ddk.keys()))
        print(list(self.ddk.values()))

    def app2(self):
        value_list = []
        keys_list = list()
        for k,v in self.ddk.items():
            keys_list.append(k)
            value_list.append(v)
        return keys_list, value_list

    def app3(self):
        vv_li = []
        ky_li = []
        list(map(lambda pair :(vv_li.append(pair[1]), ky_li.append(pair[0])), self.ddk.items()))
        print(vv_li)
        print(ky_li)



dic_values = {int(x):int(x)*2 for x in input("Enter the values: ").split()}
obj = Working14(dic_values)
obj.app1()
tu = obj.app2()
print(tu[0])
print(tu[1])

obj.app3()

