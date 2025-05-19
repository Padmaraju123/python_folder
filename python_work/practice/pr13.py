# Create a list of tuples, where each tuple contains a number and its square

class Working13:

    def __init__(self,lk):
        self.lk = lk


    def app1(self):
        tuple_values = [(x,x**2) for x in self.lk]
        return tuple_values

    def app2(self):
        return list(map(lambda x: (x,x**2),self.lk))

    def app3(self):
        print(list(range(5)))

input_list = [int(i) for i in input("Enter the values to square of each: ").split()]
obj = Working13(input_list)
print(obj.app1())
print(obj.app2())
obj.app3()