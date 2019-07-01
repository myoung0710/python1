Num = int(input("숫자를 입력하세요 : "))

sum = 0

#for i in range (0, Num+1, 1):
#    sum = sum+i
#    print(sum)

for i in range(0, Num+1, 1):
    if(i % 3 ==0):
        continue
    sum = sum +i
    print(sum)

