"""
Create a list of numbers from 1 to 10. Using a loop, print each number,
but for numbers divisible by 2, print "Even", and for numbers divisible by 3,
print "Multiple of 3".
For numbers divisible by both, print "Even & Multiple of 3".
"""

class Solution:

    def __init__(self):
        self.gt_lis = 0

    def creating_list(self):
       self.gt_lis = [i for i in range(1,11)]

    def processing_list(self):
        return [print("True") if j%2 else print("Multiple of 3") if j%3 else print("Even & Multiple of 3") for j in self.gt_lis]




obj = Solution()
obj.creating_list()
print(obj.processing_list())