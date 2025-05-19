
def func2(f1):
    print("i'm the first person")
    f1()


@func2
def func1():
    print("i'm last")


func1()

