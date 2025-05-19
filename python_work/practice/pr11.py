# Given a list of strings, create a new list with only strings longer than 3 characters.

class Working11:

    def __init__(self,wrd_li):
        self.wd_ll = wrd_li

    def app1(self):
        out_ll = []
        for ww in self.wd_ll:
            if len(ww)>3:
                out_ll.append(ww)
        return out_ll

    def app2(self):
        return [w for w in self.wd_ll if len(w) > 3]

    def app3(self):
        return list(map(self.app4, self.wd_ll))

    def app4(self, js):
        if len(js) > 3:
            return js

    def app5(self):
        return list(filter(lambda gh : len(gh)>3, self.wd_ll))

    def app6(self):
        return list(filter(self.app4, self.wd_ll))


words_list = input("Enter the words: ").split()
obj = Working11(words_list)
print(obj.app1())
print(obj.app2())
print(obj.app3())
print(obj.app5())
print(obj.app6())