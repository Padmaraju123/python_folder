# Use list comprehension to filter out odd numbers from a list of numbers.

class Working12:

    def __init__(self,liii):
        self.liii = liii

    def app1(self):
        jj = []
        for h in self.liii:
            if h%2 != 0 :
                jj.append(h)
        return jj

    def app2(self):
        return list(filter(lambda x: x%2 != 0, self.liii))

    def app3(self):
        return list(filter(lambda x: self.app4(x), self.liii))

    def app4(self,vv):
        if vv%2 != 0:
            return True




number_lis = [int(i) for i in input("Enter the number sequence: ").split()]

obj = Working12(number_lis)
print(obj.app1())
print(obj.app2())
print(obj.app3())
