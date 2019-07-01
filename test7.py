testList1 = []
testList2 = []
testList3 = []
result = ""
value  = 0

for i in range(0, 5, 1):
    for j in range(0, 5, 1):
        value += 3
        for k in range(1, 10, 1):
            result = str(value)+str("*")+str(k)+str("=")+str(value*k)
            testList1.append(result)
        testList2.append(testList1)
        testList1 = []
    testList3.append(testList2)
    testList2 = []

print(testList3)

