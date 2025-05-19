# a = input("Enter the sentence: ")
# b = tuple(a.split(" ",-1))
# print(b)
# c = " ".join(b)
# print(c)


#
# word = list(input("Enter the word: "))
#
# le1 = len(word)
# ws = "".join([j for j in word if j.isalpha()])
# le2 = len(ws)-1
# out = ""
#
# for i in range(le1):
#     if word[i].isalpha():
#         out=out+ws[le2]
#         le2-=1
#
#     else:
#         idx = word.index(word[i])
#         out+=word[idx]
#
# print(out)


# "hello,world! how:are you?"
# Output:
# "olleh,dlrow! woh:era uoy?"


class Working37:
    def __init__(self,pt):
        self.pt = pt

    def operation(self):
        out = []
        wrd = ""
        for i in range(len(self.pt)):
            if self.pt[i].isalpha():
                wrd+=self.pt[i]
            else:
                out.append(wrd[::-1])
                out.append(self.pt[i])
                wrd = ""
        print("".join(out))



put = input("Enter the value: ")  #hello,world! how:are  you?
obj = Working37(put)
obj.operation()
