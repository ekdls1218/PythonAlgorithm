# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
    # 테스트 케이스 개수 입력 받기기
inputTcCount = int(input(""))

aPlusBList = []
for tcc in range(inputTcCount):
    inputNum = input("").split()
    aPlusBList.append(int(inputNum[0]) + int(inputNum[1]))

for apb in aPlusBList:
    print(apb)
