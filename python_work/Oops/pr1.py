class Parent:

    surname = "Ayyappa"

    def __init__(self):
        self.age = 30


class Working(Parent):

    surname = "Siddanatham "  # class attribute
    print("The class attribute is {}".format(surname))

    def __init__(self,n,a):           # constructor or special method or dunder method
        self.fullname = self.__class__.surname+n               # instance attribute
        self.age = a

    # instance method
    def inst_meth1(self):
        print(self.fullname)
        print(self.age)

        # to access the class attributes inside the methods we follow like self.__class__.attribute
        print("The surname of the family is {}".format(self.__class__.surname))

        # another way to access the class attribute is class_name.attribute
        print("The another way for access the class attribute is {}".format(Working.surname))


    # class method use cls parameter instead of self and use @classmethod decorator to define class method
    @classmethod
    def cla_meth1(cls,occupation):
        print("My occupation is {}".format(occupation))


    @staticmethod
    def sta_meth1(a,b):
        print(a+b)





name = input("Enter the name: ")
age = int(input("Enter the age: "))
obj = Working(name,age)


## accessing the instance attributes outside the class
print("Accessing the fullname outside the class {}".format(obj.fullname))

## accessing the class attributes outside the class
print("Accessing the surname outside the class {}".format(obj.surname))

obj.inst_meth1()



given_occupation = input("Enter the occupation: ")
obj.cla_meth1(given_occupation)

# accessing the static method
Working.sta_meth1(10,20)