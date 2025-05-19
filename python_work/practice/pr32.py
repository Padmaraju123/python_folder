class Working32:

    def __init__(self,lis_num, em_dik):
        self.lk_num = lis_num
        self.ep_dk = em_dik

    def app1(self):
        kk = list(map(lambda n:self.ep_dk["Even"].append(n) if n%2==0 else self.ep_dk["odd"].append(n), self.lk_num))
        return self.ep_dk
    def app2(self):
        # different question
        out = ["raju","msys"]+["tech"]
        print(out)





list_num = [int(i) for i in input("Enter the numbers sequence: ").split()]
emp_dik = {ww:[] for ww in ["Even","odd"]}
obj = Working32(list_num,emp_dik)
print(obj.app1())
obj.app2()
