from model import areaXYDao
from service.api.sensibletemperature.formatConvertor import formatConvertor
from service.api.sensibletemperature.sensibleTemperatureApi import sensibleTemperatureApi
from datetime import datetime, timedelta

from service.api.shorttermforecast.ForecastTypeEnum import ForecastType
from service.api.shorttermforecast.shortTermWeatherForecastApi import ShortTermWeatherForecastApi
from service.util.definitionRisk import check_risk


def get_today_minus_1():
    convertor = formatConvertor()
    today = convertor.datetime_to_string(datetime.today() - timedelta(hours=1))
    return today



def get_SKY_PTY_T1H_in_short_term_forecast(x=37, y=126):
    today = get_today_minus_1()
    ymd = today[0:6]
    time = today[6:] + '00'
    api = ShortTermWeatherForecastApi(x, y, ymd, time)  # API 기본 Configuration (x, y, 검색날짜, 검색시간)
    response = api.request_api()  # response 값 API 요청
    SKY = api.find_category_from_response(response,
                                          ForecastType.SKY.name)  # response 값에서 카테고리에 따른 값 (카테고리 확인 : ForecastTypeEnum), Default=RN1

    PTY = api.find_category_from_response(response,
                                          ForecastType.PTY.name)  # response 값에서 카테고리에 따른 값 (카테고리 확인 : ForecastTypeEnum), Default=RN1
    T1H = api.find_category_from_response(response,
                                          ForecastType.T1H.name)  # response 값에서 카테고리에 따른 값 (카테고리 확인 : ForecastTypeEnum), Default=RN1
    return SKY, PTY, T1H


def get_sensible_temp_present(time_range):
    convertor = formatConvertor()
    today = get_today_minus_1()

    api = sensibleTemperatureApi(today)  # api configuration
    response = api.request_api()  # api 신청
    convertor.setData(response)  # 컨버터 등록
    response = convertor.execute()  # 컨버터 실행

    print(convertor.get_predict_list_data(time_range, today))


def get_info_from_address(address):  # 구, 동 으로 정보를 찾아냄. 정보가 없으면 구로만 검색한 결과를 뿌려줌
    addList = address.split(' ')
    gu, dong = addList[1], addList[2]
    return areaXYDao.findareaXYBygudong(gu, dong)


def check_weather(data):
    return check_risk(data)


if __name__ == '__main__':
    print(get_info_from_address(address="제주특별자치도 서귀포시 가가로 14"))
    get_sensible_temp_present(6)
