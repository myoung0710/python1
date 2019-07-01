import random

ArrNum = []
Throwcount = 0
matchCount =0

while matchCount != 2:
    Throwcount += 1
    ArrNum.append((random.randrange(1, 6)))
    ArrNum.append((random.randrange(1, 6)))
    ArrNum.append((random.randrange(1, 6)))
    ArrNum.append((random.randrange(1, 6)))
    ArrNum.append((random.randrange(1, 6)))
    ArrNum.append((random.randrange(1, 6)))
    print(ArrNum)
    if ArrNum[0] == ArrNum[1] == ArrNum[2] == ArrNum[3] == ArrNum[4] == ArrNum[5]:
        matchCount+=1
    ArrNum = []

print(Throwcount)
