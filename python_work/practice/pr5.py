#Access the first, last, and middle elements of a list.

class Working:

    def __init__(self):
        self.li = 0

    def generate_list(self):
        self.li = list(range(11))
        print(self.li)

    def app1(self):
        print("The first number is {}".format(self.li[0]))
        print("The last number is {}".format(self.li[-1]))
        print("The middle number is {}".format(self.li[len(self.li)//2]))




obj = Working()
obj.generate_list()
obj.app1()