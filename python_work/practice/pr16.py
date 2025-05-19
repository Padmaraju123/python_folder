number = "8142845339"

# with out function
le = len(number)
vv = 0
while le>1:
    for i in number:
        vv+=int(i)
    number = str(vv)
    le = len(number)
    vv = 0
print(int(number))



