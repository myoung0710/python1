LastNum = int(input())

for Upper in range(1, LastNum+1, 1):
    for i in range(0, LastNum+1-Upper, 1):
        print(" ", end = "")
    for j in range(0, Upper*2-1, 1):
        print("*", end="")
    print("")

for Lower in range(LastNum-1, 0, -1):
    for i in range(LastNum+1-Lower, 0, -1):
        print(" ", end="")
    for j in range(Lower*2-1, 0, -1):
        print("*", end="")
    print("")