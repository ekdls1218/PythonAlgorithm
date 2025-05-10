import sys

testCount = int(input(""))
for tc in range(testCount):
    s = sys.stdin.readline().strip().split()
    aPlusB = int(s[0]) + int(s[1])
    print(aPlusB)
