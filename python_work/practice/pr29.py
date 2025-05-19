# Python program to print even length words in a string

class Working29:
    def __init__(self,lt):
        self.lt = lt

    def app1(self):
        for tt in self.lt:
            le = len(tt)
            if le%2 == 0:
                print(le,tt)




lt = input("Enter the word sequence: ").split()

obj = Working29(lt)
obj.app1()