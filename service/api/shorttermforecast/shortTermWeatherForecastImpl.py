from service.api.shorttermforecast.ForecastTypeEnum import ForecastType
from service.api.shorttermforecast.shortTermWeatherForecastApi import ShortTermWeatherForecastApi

# for test
# result = 원하는 시간으로부터 6시간의 데이터
def print_result(result):
    for value in result:
        print(value)
if __name__ == '__main__':
    api = ShortTermWeatherForecastApi(37, 126, '20220713', '0630') # API 기본 Configuration (x, y, 검색날짜, 검색시간)
    response = api.request_api() # response 값 API 요청
    result = api.find_category_from_response(response, ForecastType.SKY.name) # response 값에서 카테고리에 따른 값 (카테고리 확인 : ForecastTypeEnum), Default=RN1
    print_result(result)

    result = api.find_category_from_response(response, ForecastType.PTY.name)  # response 값에서 카테고리에 따른 값 (카테고리 확인 : ForecastTypeEnum), Default=RN1
    print_result(result)

    result = api.find_category_from_response(response,
                                             ForecastType.T1H.name)  # response 값에서 카테고리에 따른 값 (카테고리 확인 : ForecastTypeEnum), Default=RN1
    print_result(result)