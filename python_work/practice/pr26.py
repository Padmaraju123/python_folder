"""

Python program to check whether the string is Symmetrical or Palindrome

The task of checking whether a string is symmetrical or palindrome in Python involves two main operations .
A string is symmetrical if its first half matches the second half,
considering the middle character for odd-length strings.
A string is palindrome if it reads the same forward and backward.

For example, with s = “amaama”, the first half “ama” matches the second half “ama”, making it symmetrical.
Also, since “amaama” reads the same in both directions, it is a palindrome.
However, for s = “abcba”, it is a palindrome but not symmetrical, as “ab” is not equal to “ba”.
"""

class Working26:

    def __init__(self,wrd):
        self.wrd = wrd
        self.le = len(self.wrd)
        self.half_le = self.le//2

    def app1(self):
        if self.le%2 != 0:
            first_half = self.wrd[:self.half_le+1]
            second_half = self.wrd[self.half_le:]
        else:
            first_half = self.wrd[:self.half_le]
            second_half = self.wrd[self.half_le:]

        print(first_half, second_half)

        return first_half, second_half

    def app2(self):
        out = self.app1()
        if out[0] == out[1]:
            print("Given word is symmetrical: ")
        else:
            reverse_second_half = out[1][::-1]
            if out[0] == reverse_second_half:
                print("Palindrome")
            else:
                print("Given word is neither symmetrical nor palindrome")



word = input("Enter the word: ")
obj = Working26(word)
obj.app1()
obj.app2()
