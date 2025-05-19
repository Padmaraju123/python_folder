
d = dict([["a",100],["b",200]])

# handling the key error in dictionary

try:
    print(d["c"])
    
except:
    raise KeyError("There is KeyValue error")
