from service.api.ForecastTypeEnum import ForecastType
from service.api.shortTermWeatherForecastApi import ShortTermWeatherForecastApi

# for test
# result = 원하는 시간으로부터 6시간의 데이터
if __name__ == '__main__':
    api = ShortTermWeatherForecastApi(60, 127, '20220712', '0900') # API 기본 Configuration (x, y, 검색날짜, 검색시간)
    response = api.request_api() # response 값 API 요청
    result = api.find_category_from_response(response, ForecastType.REH.name) # response 값에서 카테고리에 따른 값 (카테고리 확인 : ForecastTypeEnum), Default=RN1

    for value in result:
        print(value)
