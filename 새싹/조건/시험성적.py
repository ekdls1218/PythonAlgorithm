# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

testScore = int(input(""))

if(testScore <= 100 and testScore >= 90):
    print("A")
elif(testScore <= 89 and testScore >= 80):
    print("B")
elif(testScore <= 79 and testScore >= 70):
    print("C")
elif(testScore <= 69 and testScore >= 60):
    print("D")
else:
    print("F")

