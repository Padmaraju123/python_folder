"""
Convert numeric words to numbers

The goal is to convert numeric words (such as “zero”, “one”, “two”, etc.)
into their corresponding digit forms (e.g., “0”, “1”, “2”) to facilitate numerical operations.
For example, in the string “zero four zero one”, we aim to convert it into the string “0401”.
 Let’s explore different approaches to achieve this conversion.
"""

class Working19:

    def __init__(self, dk1, numbers_words):
        self.dk1 = dk1
        self.numbers_words = numbers_words

    def app1(self):
        ff = ""
        for vv in self.numbers_words:
            if vv in self.dk1:
                ff+=self.dk1[vv]
        print(int(ff))

    def app1(self):
        



# creating dictionary
tpp = list()
for vv in range(10):
    tp = input("enter the values: ").split()
    tpp.append(tp)

dk1 = dict(tpp)
numbers_words = input("Enter the numbers: ").split()
obj = Working19(dk1,numbers_words)
obj.app1()





