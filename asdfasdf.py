import operator

test1 = "내가 그의 이름을 불러주기 전에는 그는 다만 하나의 몸짓에 지나지 않았다. 내가 그의 이름을 불러주었을때, 그는 내게로 와 꽃이 되었다." \
        "내가 그의 이름을 불러주었을 때,그는 내게로 와 꽃이 되었다." \
        "내가 그의 이름을 불러준 것처럼 나의 이 빛깔과 향기에 알맞는 누가 나의 이름을 불러다오." \
        "그에게로 가서 나도 그의 꽃이 되고 싶다. 우리들은 모두 무엇이 되고싶다." \
        "나는 너에게 너는 나에게 잊혀지지 않는 하나의 눈짓이 되고 싶다."
CountDic = {}
CountList =[]

if __name__ == "__main__":
    for ch in test1:
        if '가' <= ch and ch <= '힣':
            if ch in CountDic:
                CountDic[ch] +=1
            else:
                CountDic[ch] = 1
    CountList = sorted(CountDic.items(), key = operator.itemgetter(1), reverse=True)

    print("원문\n", test1)
    print("================================")
    print("문자\t빈도수")
    print("================================")
    for i in range(0, len(CountList)):
        print(CountList[i][0], "\t", CountList[i][1])

