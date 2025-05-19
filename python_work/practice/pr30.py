class Working30:

    def __init__(self,lk):
        self.lk = lk
        self.le = len(self.lk)

    def app1(self):
        for i in range(0,self.le):
            for j in range(0,self.le-i-1):
                if self.lk[j] > self.lk[j+1]:
                   self.lk[j] , self.lk[j+1] = self.lk[j+1], self.lk[j]
            print(self.lk)
        return self.lk



lis_num = list(map(int, input("Enter the number sequence: ").split())) # 2 3 -5 -7 9 4 6 -1 -8 0
obj = Working30(lis_num)
print(lis_num)
print("The final sorted list is {}".format(obj.app1()))
