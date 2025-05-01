# 서울의 오늘 날짜를 출력하는 프로그램을 작성하시오.
# 오늘 날짜 YYYY-MM-DD로 출력

import datetime 

now  = datetime.datetime.now()
print(now.strftime("%Y-%m-%d"))
