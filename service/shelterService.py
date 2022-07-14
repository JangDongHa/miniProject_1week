from wsgiref import headers

import requests

from service.api.heatshelter import shelterApi
from flask import request, jsonify
from service.tempService import get_info_from_address
from service.userService import get_jwt_user_info

def get_headers():
    return {
        "X-NCP-APIGW-API-KEY-ID": "6rjx5nfk5b",
        "X-NCP-APIGW-API-KEY": "t7NmX2QiLTTkXmf1ZfE2iWSAuDERQ0JhpQXFDD2m"
    }

def get_shlter_data(request):
    token = request.cookies.get('mytoken')
    user_info = get_jwt_user_info(token)
    address = user_info['address']
    areaNo = get_info_from_address(address)['areaNo']

    if str(areaNo)[5:] == "00000": # 데이터가 없는 얘들 공통점인데 나중에 수정 예정
        change_area = areaNo + 51000
        areaNo = str(change_area)
    data = shelterApi.setting_data(areaNo)
    result = shelterApi.get_all_equptype_data(data)  # 형태 : list({},{},{}....)
    return shelterApi.get_need_result(result)  # 그 중에서 필요한 데이터만 정제한 것

def current_location():
    token = request.cookies.get('mytoken')
    user_info = get_jwt_user_info(token)
    address = user_info['address']

    r = requests.get(f"https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={address}",
                     headers=get_headers())
    response = r.json()
    try: #네이버 검색 결과 없을 떄
        x = response["addresses"][0]["x"]
        y = response["addresses"][0]["y"]
    except:
        x = 0
        y = 0

    current_location = {
        'address': address,
        'xcord': x,
        'ycord': y
    }

    return jsonify({'current_location': current_location})