class Working21:
    def __init__(self,lst):
        self.lst = lst

    def app1(self):
        self.lst.sort()
        print("""The sorted list is {0}\nThe second highest value of the given list is {1}""".format(self.lst,self.lst[-2]))



lst = list(map(int,input("enter the number sequence: ").split()))
print(lst)
obj = Working21(lst)
obj.app1()