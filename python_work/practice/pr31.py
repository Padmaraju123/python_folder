class Working31:

    def __init__(self,wrd_lst):
        self.wrd_lst = wrd_lst
        self.out_list = []


    def app1(self):
        for ww in self.wrd_lst:
            le = len(ww)
            if le%2!= 0 and ww[:le//2] == ww[le//2+1:][::-1]:
                self.out_list.append(ww)
            else:
                if ww[:le//2] == ww[le//2:][::-1]:
                    self.out_list.append(ww)
        return self.out_list


words_list = input("Enter the word sequence: ").split()
obj = Working31(words_list)
print("This list of palindromes are {}".format(obj.app1()))
