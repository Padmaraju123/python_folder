#Count occurrences of an element in a list in Python
class TestWork:

    def __init__(self,l):
        self.li = l

    def test_meth1(self):
        print(self.li)




lis = [int(i) for i in input("Enter the number sentence with one space: ").split(" ")]
obj = TestWork(lis)
obj.test_meth1()
