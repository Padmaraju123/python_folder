# Slice a list to get the first 5 elements.

class Working:

    def __init__(self, n, listt):
        self.n = n
        self.listt = listt

    def app1(self):
        return self.listt[:self.n]

    def app2(self):
        lk = list()
        for i in range(self.n):
            lk.append(self.listt[i])
        return lk

    def app3(self):
        return list(map(lambda i:self.listt[i], range(self.n)))





List_vv = [int(i) if i.isdigit() else i for i in input("Enter the values with both integer and words: ").split()]
n = int(input("Enter the value to slice upto in the list: "))
obj = Working(n, List_vv)
print("The list after the sliced in app1: {}".format(obj.app1()))
print("The list after the sliced in app2: {}".format(obj.app2()))
print("The list after the sliced in app3: {}".format(obj.app3()))

