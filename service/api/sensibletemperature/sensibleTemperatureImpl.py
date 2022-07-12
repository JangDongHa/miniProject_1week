from service.api.sensibletemperature.formatConvertor import formatConvertor
from service.api.sensibletemperature.sensibleTemperatureApi import sensibleTemperatureApi


if __name__ == '__main__':
    api = sensibleTemperatureApi('2022071112') # api configuration
    response = api.request_api() # api 신청
    convertor = formatConvertor(response) # 컨버터 등록
    response = convertor.execute() # 컨버터 실행

    print(response) # 원본 값
    print(convertor.data_to_custom_predict_data(6)) # 원하는 범위까지의 값


