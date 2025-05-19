
# li = [2,3,0,1] le = 4
class Working:

    def __init__(se,num):
        se.num = num
        se.le = len(num)

    def processing(self):

        for i in range(self.le):
            for j in range(i+1,self.le):
                if self.num[i] > self.num[j]:
                    self.num[j], self.num[i] = self.num[i], self.num[j]
        print(self.num[-1])



num_seq = list(map(int,input("enter the num seq: ").split(" ")))

for i in num_seq:
    print(i)

# obj = Working(num_seq)
# obj.processing()
