# Write a program in Python to remove duplicate elements form array without using inbuilt function.
class Working22:

    def __init__(self, list_num):
        self.ll = list_num

    def app1(self):
        undup = []
        for i in self.ll:
            if i not in undup:
                undup.append(i)
        print(undup)
        return undup

    def app2(self):
        dk = {}
        for j in self.ll:
            if j not in dk:
                dk[j] = True
        print(dk)


    def app3(self):
        out_l = self.app1()
        given_in = int(input("Enter the index value to delete list value: "))
        vk = out_l[given_in]
        out_l.remove(vk)
    




list_num = list(map(int,input("Enter the number sequence: ").split()))
obj = Working22(list_num)
obj.app1()
obj.app2()
obj.app3()