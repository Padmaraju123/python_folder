"""
Given a string of size n, write functions to perform following operations on string:

Left (Or anticlockwise) rotate the given string by d elements (where d <= n).
Right (Or clockwise) rotate the given string by d elements (where d <= n).
For example, let’s take a string s = “GeeksforGeeks”
and d = 2, so for this example, our Left Rotation will be “eksforGeeksGe”
and Right Rotation will be “ksGeeksforGee”. Let’s discuss some of the ways to do it with examples.
"""

class Working35:

    def __init__(self,word,num):
        self.word = word
        self.n = num
        self.le = len(word)

    def app1(self):
        rev_out1 = self.word[self.le-self.n:]+self.word[:self.le-self.n]
        print(rev_out1)

    def app2(self):
        rev_out2 = self.word[-self.n:]+self.word[:-self.n]
        print(rev_out2)



Word, n = input("Enter the word: "), int(input("Enter the number to rotate: "))
obj = Working35(Word,n)
obj.app1()
obj.app2()