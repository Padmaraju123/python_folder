# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
set_val = {int(i) for i in input().split(" ")}
N = int(input())
print(set_val)
for cmd in range(N):

    cmd_1, cmd_2 = input().split(" ")

    if cmd_1 == "remove":
        set_val.remove(int(cmd_2))
    elif cmd_1 == "discard":
        set_val.discard(cmd_2)
    else:
        set_val.pop()

print(sum(set_val))


