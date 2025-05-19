
def wrap(string, max_width):
    le = len(string)
    out = ""
    for i in range(0,le,max_width):
        print(i)
        out+=string[i:i+max_width]+" "
        print(out)
    return out

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    # print(result)