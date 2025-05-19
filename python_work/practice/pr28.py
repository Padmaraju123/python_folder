# How to Remove Letters From a String in Python

class Working28:

    def __init__(self,word,letter):
        self.word = word
        self.letter = letter

    def app1(self):
        new_wrd = "".join([i for i in self.word if self.letter != i])
        print(new_wrd)

    def app2(self):
        out = ""
        for j in self.word:
            if j !=self.letter:
                out+=j
        print(out)

    def app3(self):
        outt = "".join(map(lambda x: "" if x==self.letter else x, self.word))
        print("The app3 output is {}".format(outt))


    def app5(self):
        outt1 = "".join(filter(lambda x: x!=self.letter, self.word))
        print(f"The app5 output is {outt1}")

    def app6(self):
        outt = "".join(filter(self.app7, self.word))
        print(outt)

    def app7(self,v):
        return v!=self.letter

    def app8(self):
        print("The app8 output is {}".format(self.word.replace(self.letter,"")))


word = input("Enter the word: ")
letter = input("Enter the letter: ")
obj = Working28(word,letter)
obj.app1()
obj.app2()
obj.app3()
obj.app5()
obj.app6()
obj.app8()
