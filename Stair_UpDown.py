Num = int(input())

for Upper in range(0, Num+1, 1):
    for i in range(0, Upper, 1):
        print("*", end="")
    print("")

for Lower in range(Num-1, 0, -1):
    for i in range(Lower, 0, -1):
        print("*",end="")
    print("")