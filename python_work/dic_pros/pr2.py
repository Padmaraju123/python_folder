
# d = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15}

# d = dict((("ravi",10),("rajnish",9),("sanjeev",15)))

#app1
    # out_dk = dict()
    # ar_keys = list(d.keys())
    # ar_keys.sort()
    # print(ar_keys)
    #
    # for key in ar_keys:
    #     out_dk[key]=d[key]
    # print(out_dk)

#app2

    # sorted_keys = sorted(list(d.keys()))
    #
    # out_dk = {k:d[k] for k in sorted_keys}
    # print(out_dk)

#app3

d = {"ravi": 10, "rajnish": 9, "sanjeev": 15}
out_dk = {key: d[key] for key in sorted(d, reverse=True)}
print(out_dk)


