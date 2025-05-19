# Create a list of strings and access the 3rd element.

class WK1:

    def __init__(self,wl,i):
        self.wsl = wl
        self.given_i = i

    def app1(self):
        return "The result from the app1 is {}".format(self.wsl[self.given_i])

    def app2(self):
        try :
            return "The result from the app2 is {}".format(self.wsl[self.given_i])
        except IndexError:
            return "Given index value is out of list"






# words_list = [ww for ww in input("Enter the words list ").split(" ")]
words_list = input("Enter the words list: ").split()
given_index = int(input("Enter the index value to get the value from the list: "))

obj = WK1(words_list, given_index)
# print(obj.app1())
print(obj.app2())