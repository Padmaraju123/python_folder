# Count Occurance of Substring in a List of Strings – Python
import pytest


class Work:
    def __init__(self,lss,sub):
        self.wrds = lss
        self.sb = sub

    def meth1(self):
        count = 0
        for wrd in self.wrds:
            if self.sb in wrd:
                count+=1
        return count

    def meth2(self):
        print(len(list(filter(self.meth3,self.wrds))))


    def meth3(self,n):
        if self.sb in n:
            return True
        else:
            return False




lis_words = input("Enter the words sentence ").split(" ")
sub_string = input('Enter the substring')
obj = Work(lis_words,sub_string)
print(obj.meth1())

obj.meth2()