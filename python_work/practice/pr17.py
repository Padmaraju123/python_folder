# Check if String Contains Substring in Python

class Working17:

    def __init__(self, strg, sub):
        self.strg = strg
        self.sb = sub

    def app1(self):
        try:
            assert self.sb in self.strg
        except AssertionError:
            return "False"

    def app2(self):
        if self.sb in self.strg:
            return "True"
        else:
            return "False"

    def app3(self):
        list_ww = self.strg.split()
        c = list_ww.count(self.sb)
        if c > 0:
            return "Sub string present in main string"
        else:
            return "Sub string not present in main string"

    def app4(self):
        # input strings str1 and substr
        string = "geeks for geeks"  # or string=input() -> taking input from the user
        substring = "geeks"  # or substring=input()

        # splitting words in a given string
        s = string.split()

        # checking condition
        # if substring is present in the given string then it gives output as yes
        if substring in s:
            print("yes")
        else:
            print("no")


string_sent = input("Enter the sentence: ")
sub_str = input("Enter the substring to check: ")

obj = Working17(string_sent,sub_str)
print(obj.app1())
print(obj.app2())
print(obj.app3())
obj.app4()