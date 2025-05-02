# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
    # 아무것도 입력이 안되어있을 때(EOFEError일 때) 출력

try:
    aPlusBList = []
    while(True):
        inputNum = input("")
        inputNum = inputNum.split()
        aPlusBList.append(int(inputNum[0]) + int(inputNum[1]))
except:
    for apb in aPlusBList:
        print(apb)