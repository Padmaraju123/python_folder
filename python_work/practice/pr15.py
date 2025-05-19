word = input("Enter the word to convert list of letters: ")
print(list(word))

ll  = []
for i in word:
    ll.append(i)
print(ll)

le = len(word)
i = 0
wh_ll = list()
while i<le:
    wh_ll.append(word[i])
    i+=1

print(wh_ll)

print([s for s in word])

print([*word])
print(list(map(str, word)))


c = "8142634456"

# with out function
le = len(c)
while le>1:
    c = 0
    for i in c:
        c+=int(i)
    print(c)