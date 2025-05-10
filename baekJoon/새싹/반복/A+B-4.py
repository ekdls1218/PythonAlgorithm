# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
    # 아무것도 입력이 안되어있을 때(EOFError일 때) 출력
import sys
while(True):
    try:
        inputNum = sys.stdin.readline().strip().split()
        print(int(inputNum[0]) + int(inputNum[1]))
    except:
        break