from flask import Flask, render_template, request, jsonify
import requests

from service.api.heatshelter import shelterApi




def start(app, data=''):
    headers = {
        "X-NCP-APIGW-API-KEY-ID": "6rjx5nfk5b",
        "X-NCP-APIGW-API-KEY": "t7NmX2QiLTTkXmf1ZfE2iWSAuDERQ0JhpQXFDD2m"
    }

    @app.route('/shelter', methods=["GET"])
    def get_shelter_location():
        url = 'http://apis.data.go.kr/1741000/HeatWaveShelter2/getHeatWaveShelterList2'
        data = shelterApi.setting_data('4687025000')
        result = shelterApi.get_all_equptype_data(url, data)  # 형태 : list({},{},{}....)
        myData = shelterApi.get_need_result(result)  # 그 중에서 필요한 데이터만 정제한 것

        return jsonify({'msg': 'hello', 'shelter_info': myData})

    @app.route('/current', methods=["GET"])
    def get_current_location():
        address = "서울 마포구 와우산로21길 36-6" #임시 현재 주소

        # print(address)

        r = requests.get(f"https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={address}",
                         headers=headers)
        response = r.json()
        print(response)
        x = response["addresses"][0]["x"]
        y = response["addresses"][0]["y"]

        current_location = {
            'address': address,
            'xcord': x,
            'ycord': y
        }
        # print(current_location)

        return jsonify({'current_location': current_location})