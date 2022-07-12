from enum import Enum


class ForecastType(Enum):
    RN1 = '1시간 강수량'
    PTY = '강수형태'
    REH = '습도'
    T1H = '기온'
    SKY = '하늘상태'
    PTY_CODE = {
        '0': '없음',
        '1': '비',
        '2': '비/눈',
        '3': '비/눈',
        '5': '빗방울',
        '6': '빗방울눈날림',
        '7': '눈날림'
    }
    SKY_CODE = {
        '1': '맑음',
        '3': '구름많음',
        '4': '흐림'
    }

    def convert_PTY_code(self, value):
        return self.PTY_CODE.value.get(value)

    def convert_SKY_code(self, value):
        return self.SKY_CODE.value.get(value)


if __name__ == '__main__':
    pass
