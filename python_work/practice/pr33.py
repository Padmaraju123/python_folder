class Working33:

    def __init__(self,w_list):
        self.ww_lt = w_list

    def app1(self):
        le = len(self.ww_lt)
        for i in range(le):
            for j in range(0,le-i-1):
                if ord(self.ww_lt[j][-1]) > ord(self.ww_lt[j+1][-1]):
                    self.ww_lt[j] , self.ww_lt[j+1] = self.ww_lt[j+1], self.ww_lt[j]
        print(self.ww_lt)



ww_list = input("Enter the words sequence: ").split()
obj = Working33(ww_list)
obj.app1()