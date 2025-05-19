# Slice a list to get all even-indexed elements.

class Working8:

    def __init__(self,eve_odd):
        self.eve_odd = eve_odd
        self.le = len(self.eve_odd)

    def app1(self):
        result_list = []
        for i in range(self.le):
            if i%2 == 0:
                result_list.append(self.eve_odd[i])
        return result_list

    def app2(self):
        return [self.eve_odd[i] for i in range(self.le) if i%2 == 0]

    def app3(self):
        a = list(enumerate(self.eve_odd))
        print(a)
        b = list(filter(lambda x:x[0]%2==0, a))
        print(b)
        return list(map(lambda x: x[1],b))



list_even_odd = input("Enter the words: ").split()
obj = Working8(list_even_odd)
print(obj.app1())
print(obj.app2())
print(obj.app3())