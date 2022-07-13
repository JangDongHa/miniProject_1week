import requests


class sensibleTemperatureApi:
    def __init__(self, base_time, areaNo='1100000000'):
        self.configuration(base_time, areaNo)

    def configuration(self, base_time, areaNo): #base_time = 2022010318 <-
        self.key = "wFaw7OFBqe4265nYPtDX2VQSJQke95gx56upeVRviZyp2TSZis/KZBM8Sc6fZwq8aF6vzD3HjIB3lzLOJBGYSQ=="
        self.url = "http://apis.data.go.kr/1360000/LivingWthrIdxServiceV2/getSenTaIdxV2"

        self.data = {
            'serviceKey': self.key,
            'numOfRows': 10,
            'pageNo': 1,
            'dataType': 'JSON',
            'areaNo': areaNo,  # 지점위치(참고: 지역별 지점코드(20220103).xlsx)
            'time': base_time,
            'requestCode': 'A41'  # A41 : 노인 (requestCode: 체감온도 대상. 일반인은 없고 어린이, 농촌, 건설현장 등.. 만 있어서 노인으로 함)
        }

    def request_api(self):
        r = requests.get(self.url, params=self.data)
        response = r.json()
        print(r.json())

        return response