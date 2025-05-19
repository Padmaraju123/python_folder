if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))

    le = len(arr)

    for i in range(le):
        for j in range(i + 1, le):
            if arr[i] > arr[j]:
                arr[j], arr[i] = arr[i], arr[j]

    print(arr)






