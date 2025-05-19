# Reverse a list using slicing.
class Working9:

    def __init__(self,ll):
        self.ll = ll
        self.le = len(self.ll)

    def app1(self):
        return self.ll[::-1]

    def app2(self):
        ret_li = list()
        for n in range(self.le-1,-1,-1):
            ret_li.append(self.ll[n])
        return ret_li

    def app3(self):
        return list(map(lambda x:self.ll[x],range(self.le-1,-1,-1)))


list_wrds_num = [int(i) if i.isdigit() else i for i in input("enter the words: ").split()]
obj = Working9(list_wrds_num)
print(obj.app1())
print(obj.app2())
print(obj.app3())