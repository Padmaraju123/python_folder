"""
Given two strings s1 and s2. The task is to find out the minimum number of string rotations
for the given string s1 to obtain the actual string s2. Examples:

Input : eeksg, geeks
Output: 1
Explanation: g is rotated left to obtain geeks.

Input : eksge, geeks
Output: 2
Explanation : e and g are left rotated to obtain geeks.
"""

class Working36:

    def __init__(self,a,b,lii):
        self.a = a
        self.b = b
        self.li = lii


    def app1(self):
        try:
            return self.li[9]

        except ZeroDivisionError:
            return "there is an Zero division error"

        except TypeError:
            return "There is Type error"

        except:
            return "There is Index error"






obj = Working36(10,"0",[1,2,3])
print(obj.app1())

