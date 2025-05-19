if __name__ == '__main__':
    dk = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dk[name] = score

    values = list(set(dk.values()))
    values.sort()
    check_val = values[1]


    filtered_names= [nam for nam in dk.keys() if dk[nam]==check_val]
    filtered_names.sort()
    print(filtered_names)



