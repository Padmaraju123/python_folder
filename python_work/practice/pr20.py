"""
Word location in String – Python

Word location in String problem in Python involves finding the position of a specific word
 or substring within a given string. This problem can be approached using various methods
 in Python, such as using the find(), index() methods or by regular expressions with the re module.
"""

class Working20:
    def __init__(self, words_list, sub):
        self.ws = words_list
        self.sub = sub
        self.le = len(self.sub)

    def app1(self):
        out = " ".join(self.ws)
        pos = out.find(self.sub)
        print(pos)
        try:
            if pos == -1:
                raise ValueError("The given substring is not present")

            print("The output is {}".format(out[pos:pos + self.le]))
        except ValueError as v:
            print(v)

        return pos


    def app2(self):
        pass






words_list = input("Enter the word sequence: ").split()
sub_str = input("Enter the substring: ")
obj = Working20(words_list,sub_str)
obj.app1()