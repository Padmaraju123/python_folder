"""
Python | Split string in groups of n consecutive characters

Given a string (be it either string of numbers or characters),
write a Python program to split the string by every nth character.
"""

class Working23:
    def __init__(self,str_word, n):
        self.word = str_word
        self.n = n

    def app1(self):
        out = []
        i = 0
        le = len(self.word)
        while i < le:
            out.append(self.word[i:i+self.n])
            i = i+self.n
        print(out)



str_word = input("Enter the word: ")
n = int(input("Enter the number to split: "))
obj = Working23(str_word,n)
obj.app1()