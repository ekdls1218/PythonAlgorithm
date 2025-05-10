# 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
inputYear = int(input(""))

if((inputYear % 4 == 0 and inputYear % 100 != 0) or inputYear % 400 == 0):
    print(1)
else:
    print(0)