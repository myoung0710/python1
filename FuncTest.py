def telcheck(str):
    print(str)
    if len(str) == 11:
        return True
    else:
        return False


if __name__=="__main__":
    result = False

    tel1 = "010-4314-0071"
    tel2 = "010-4314-00"

    tel1 = tel1.replace("-", "")
    tel2 = tel2.replace("-", "")
    result = telcheck(tel1)

    if result == False:
        print("전화번호 형식이 맞지 않습니다.")

    else:
        print("전화번호 형식이 일치합니다.")