from flask import Flask, render_template, request, jsonify

from model.localDto import localDTO
from service import userService, ipService, tempService
from service.tempService import check_weather


def start(app, data=''):
    @app.route('/api/weather', methods=['GET'])  # '/' must go mainController but define here for test
    def get_api_weather():
        #address = request.args.get('address')
        #weather_data = tempService.get_weather(address)
        print('ok')
        return jsonify(weather_data = 'test')

    @app.route('/api/tempAddress', methods=['GET'])
    def get_temp_address():
        return ipService.get_address_from_ip()

    @app.route('/weather', methods=['GET'])
    def get_weather():
        address = "제주특별자치도 서귀포시 가가로 14" #jwt 로부터 받아옴
        SKY, PTY, T1H = tempService.get_SKY_PTY_T1H_in_short_term_forecast()
        print(T1H)
        return render_template('weather.html', SKY=SKY, PTY=PTY, T1H=T1H, check_weather=check_weather)

    @app.route('/weather/<local>', methods=['GET'])
    def get_local_weather(local):
        SKY, PTY, T1H = tempService.get_SKY_PTY_T1H_in_short_term_forecast(localDTO['cords'][local][0], localDTO['cords'][local][1])
        return render_template('weather.html', SKY=SKY, PTY=PTY, T1H=T1H, check_weather=check_weather, address=localDTO['address'][local])

