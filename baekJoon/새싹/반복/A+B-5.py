# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
    # 입력 마지막에 0 0 입력
import sys 

while(True):
    inputNum = sys.stdin.readline().strip()
    if(inputNum == "0 0"):
        break
    inputNum = inputNum.split()
    print(int(inputNum[0]) + int(inputNum[1]))
