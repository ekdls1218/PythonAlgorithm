# 서브도메인의 유명도는 정수이다. 두 서브도메인의 유명도가 주어졌을 때, 그 차이를 구하는 프로그램을 작성하시오.
inputNum = input("").split()
result = int(inputNum[0]) - int(inputNum[1])

if(result < 0):
    print(result * (-1))
else:
    print(result)