# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

inputNum = input("").split()
a, b = int(inputNum[0]), int(inputNum[1])
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)