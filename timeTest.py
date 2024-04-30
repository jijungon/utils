# from datetime import datetime

# DATETIME_FORMAT_TIME = "%Y-%m-%d %H:%M:%S"
# DATETIME_FORMAT_BASE = "%Y-%m-%d"

# currtime_str = datetime.now().strftime(DATETIME_FORMAT_TIME)
# currtime = datetime.strptime(currtime_str, DATETIME_FORMAT_TIME)







# ## 문자열 저장
# currtime_str = datetime.now().strftime(DATETIME_FORMAT_TIME) ## 초단위까지
# ## datetime 객체로 변환
# datatime = datetime.strptime(currtime_str, DATETIME_FORMAT_TIME)  ## 시간타입
# # datetime 객체를 다시 문자열로 변환하여 원하는 형식으로 출력
# formatted_date_str = datatime.strftime(DATETIME_FORMAT_BASE) ## 일까지


from functools import partial
from datetime import datetime

DATETIME_FORMAT_TIME = "%Y-%m-%d %H:%M:%S"
DATETIME_FORMAT_BASE = "%Y-%m-%d"

def convert_datetime_partial(case):
    currtime_str = datetime.now().strftime(DATETIME_FORMAT_TIME)

    # if time이 있으면 그걸로 없으면 현재 시간으로

    if case == "datetime_all":
        return datetime.strptime(currtime_str, DATETIME_FORMAT_TIME)
    elif case == "datetime_str":
        return currtime_str
    elif case == "datetime_day":
        datetime_obj = datetime.strptime(currtime_str, DATETIME_FORMAT_TIME)
        return datetime_obj.strftime(DATETIME_FORMAT_BASE)

# Partial 함수 생성

# 사용 예시
datetime_all = convert_datetime_partial("datetime_all")
print("Datetime All:", datetime_all)

str_date = convert_datetime_partial("datetime_str")
print("String:", str_date)

datetime_day = convert_datetime_partial("datetime_day")
print("Datetime Day:", datetime_day)