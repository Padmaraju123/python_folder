class Work:

    def __init__(self, vall):
        self.vall = vall

    def Exception(self):
        # self.n = int(input("Enter v"))
        try:
            res = self.vall / 0
        except:
            print("it is wrong")






n = int(input("Enter the value: "))
obj = Work(n)
obj.Exception()
