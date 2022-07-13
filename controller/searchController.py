from flask import Flask, render_template, request, jsonify
import requests

def start(app, data=''):
    headers = {
        "X-NCP-APIGW-API-KEY-ID": "6rjx5nfk5b",
        "X-NCP-APIGW-API-KEY": "t7NmX2QiLTTkXmf1ZfE2iWSAuDERQ0JhpQXFDD2m"
    }

    @app.route('/shelter', methods=["GET"])
    def get_shelter_location():
        restname = "6.25참전유공자경로당"
        restaddr = "서울특별시 종로구 팔운대로 88, 지하1층 6.25참전유공자경로당(신교동)"
        equptype = "노인시설"
        usePsblNmpr = 100
        xcord = 127.0379399
        ycord = 37.4981125
        # 쉼터 API 예시
        shelter_info = [{
            'shelter_name': restname,
            'shelter_address': restaddr,
            'shelter_type': equptype,
            'shelter_max_people': usePsblNmpr,
            'xcord': xcord,
            'ycord': ycord
        }, {
            'shelter_name': "종로회당",
            'shelter_address': "종로구 종로시 종로로",
            'shelter_type': "체육시설",
            'shelter_max_people': 39,
            'xcord': 126.3241,
            'ycord': 36.9999
        }
        ]
        print(shelter_info)
        return jsonify({'msg': 'hello', 'shelter_info': shelter_info})

    @app.route('/current', methods=["GET"])
    def get_current_location():
        address = "서울 마포구 와우산로21길 36-6"

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