import requests

from service.api.shorttermforecast.ForecastFind import forecastFind
from service.api.shorttermforecast.ForecastTypeEnum import ForecastType


class ShortTermWeatherForecastApi():
    def __init__(self, x, y, base_date, base_time):
        self.configuration(x,y,base_date,base_time)

    def configuration(self, x, y, base_date, base_time):
        self.key = "YqFSfco5vUHbQReNWGXtoEXAhBLI01arfZyJjNEJ5pPEGV6qjiSydpE7lfk2SZuTEBMZt3ZEWkkBx4Btl7M59w=="
        self.url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst"
        self.data = {
            'serviceKey': self.key,  # 공공데이터포털 서비스 인증 키
            'numOfRows': 100,  # 한 페이지 결과 수 (초단기예측 : 예측시간 6~10 시까지의 데이터를 얻고 싶다면 0530기준 5, 초단기실황 : 타입 종류)
            'pageNo': 1,  # 페이지 번호
            'dataType': 'JSON',  # 요청자료형식
            'base_date': base_date,  # 발표일
            'base_time': base_time,  # 발표시간 (5시 30분, 6시 30분 ....)
            'nx': x,  # 좌표 (별첨 엑셀 참고)
            'ny': y  # 좌표 (별첨 엑셀 참고)
        }

    def request_api(self):
        r = requests.get(self.url, params=self.data)
        response = r.json()

        return response

    def find_category_from_response(self, response, apiCategory=ForecastType.RN1.name):
        forecast = forecastFind(response)  # 카테고리 검색
        result = forecast.category(apiCategory)  # 카테고리
        return result