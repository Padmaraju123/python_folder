"""
Python – Count and display vowels in a string

Given a string, we need to write a Python program that counts and displays all the vowels present in the string.
Let’s explore different ways of counting and displaying vowels in a string.

We need to identify all the vowels in the string both uppercase and lowercase.
We should display each vowel found.
We should also count how many total vowels are in the string.
"""

class Working24:

    def __init__(self,wrd):
        self.wrd = wrd.lower()

    def app1(self):
        vowel_dk = {}
        li = list(self.wrd)
        vl_list = ["a","e","i","o","u"]
        for v in li:
            # v = v.lower()
            if v in vl_list:
                cc = li.count(v)
                vowel_dk[v] = cc               #PadmArajU12@-1$$

        print(list(vowel_dk.keys()))
        print(vowel_dk)





word = input("Enter the word: ")
obj = Working24(word)
obj.app1()