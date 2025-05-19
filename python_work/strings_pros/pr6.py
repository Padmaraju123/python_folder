# Python – Words Frequency in String Shorthands

#app1
    # given_sent = input('Enter the sentence with repeated words: ')
    # dtt = dict()
    # lk = given_sent.split(" ")
    # for ww in lk:
    #     if ww not in dtt:
    #         cc = lk.count(ww)
    #         dtt[ww] = cc
    # print(dtt)

#app2
given_sent = input('Enter the sentence with repeated words: ')

lk = given_sent.split(" ")

unique_words = set(lk)

dk2 = {ww:lk.count(ww) for ww in lk }
print(dk2)






