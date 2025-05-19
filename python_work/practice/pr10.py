#Given a list of numbers, create a new list containing the squares of all numbers.

class Working10:

    def __init__(self,clss_lis):
        self.lss = clss_lis

    def app1(self):
        out_lis = list()
        for i in self.lss:
            out_lis.append(i**2)
        return out_lis

    def app2(self):
        return [j**2 for j in self.lss]

    def app3(self):
        return list(map(lambda x: x**2, self.lss))

    def app4(self):
         return list(map(self.app5, self.lss))

    def app5(self,v):
        return v**2
    



num_lis = [int(u) for u in input("Enter the number sequence: ").split()]
obj = Working10(num_lis)
print(obj.app1())
print(obj.app2())
print(obj.app3())
print(obj.app4())
