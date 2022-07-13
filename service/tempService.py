from model import areaXYDao
from service.api.sensibletemperature.formatConvertor import formatConvertor
from service.api.sensibletemperature.sensibleTemperatureApi import sensibleTemperatureApi
from datetime import datetime

def get_sensible_temp_present(time_range):
    convertor = formatConvertor()
    today = convertor.datetime_to_string(datetime.today())
    print(today)


    # api = sensibleTemperatureApi(today)  # api configuration
    # response = api.request_api()  # api 신청
    # convertor.setData(response)  # 컨버터 등록
    # response = convertor.execute()  # 컨버터 실행
    #
    # print(response)  # 원본 값
    # print(convertor.data_to_custom_predict_data(time_range))  # 원하는 범위까지의 값

def get_info_from_address(address=''): # 구, 동 으로 정보를 찾아냄. 정보가 없으면 구로만 검색한 결과를 뿌려줌
    address = "제주특별자치도 서귀포시 가가로 14"
    addList = address.split(' ')
    gu, dong = addList[1], addList[2]
    return areaXYDao.findareaXYBygudong(gu, dong)

if __name__ == '__main__':
    get_sensible_temp_present(6)
    print(get_info_from_address())