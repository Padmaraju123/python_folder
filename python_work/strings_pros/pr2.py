# Input: "aaabbc" → Output: "a3b2c1"

class Working:

    def __init__(self,w):
        self.w = w


    def app1(self):

        dic = {}
        le = len(self.w)
        c = 0
        out = ""
        for i in range(le-1):
            if self.w[i]==self.w[i+1]:
                c+=1
            else:
                out=out+self.w[i]+str(c)
                c = 0
        print(out)

    def app2(self):

        out = ""
        count = 1
        for i in range(1, len(self.w)):
            if self.w[i] == self.w[i - 1]:
                count += 1
            else:
                out += self.w[i - 1] + str(count)
                count = 1  # reset for next character
        out += self.w[-1] + str(count)  # handle last character
        print(out)


# word = input("Enter the word: ")
# obj = Working(word)
# obj.app1()
# obj.app2()\

word = "aaabcdde"
out1 = list(set(word))
out2 = list(out1)
print(out1,out2)

