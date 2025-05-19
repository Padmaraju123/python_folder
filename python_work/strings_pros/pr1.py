class Working1:

    def __init__(self,w):
        self.w = w

    def app1(self):
        lk = list(self.w)
        extra = [i for i in self.w if i.isalpha()][::-1]
        # le = len(extra)-1
        out = ""
        for w in lk:
            if w.isalpha():
                out += extra.pop(0)
                # le -= 1
            else:
                out+=w
        print(out)




word = input("Enter the word: ") # input = a,b$c, o/p = c,b$a
obj = Working1(word)
obj.app1()