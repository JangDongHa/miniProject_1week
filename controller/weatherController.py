from flask import Flask, render_template, request, jsonify, redirect, url_for

from model.localDto import localDTO
from service import userService, ipService, tempService
from service.tempService import check_weather


def start(app, data=''):
    @app.route('/api/tempAddress', methods=['GET'])
    def get_temp_address():
        return ipService.get_address_from_ip()

    @app.route('/weather', methods=['GET'])
    def get_weather():
        if (request.cookies.get('mytoken')):
            pass
        else:
            return redirect(url_for("getLogin"))
        address = userService.get_jwt_user_info(request.cookies.get('mytoken'))['address']
        info = tempService.get_info_from_address(address)
        x, y = info['x'], info['y']
        SKY, PTY, T1H = tempService.get_SKY_PTY_T1H_in_short_term_forecast(x, y)
        return render_template('weather.html', SKY=SKY, PTY=PTY, T1H=T1H, check_weather=check_weather, address=address)

    @app.route('/weather/<local>', methods=['GET'])
    def get_local_weather(local):
        SKY, PTY, T1H = tempService.get_SKY_PTY_T1H_in_short_term_forecast(localDTO['cords'][local][0], localDTO['cords'][local][1])
        return render_template('weather.html', SKY=SKY, PTY=PTY, T1H=T1H, check_weather=check_weather, address=localDTO['address'][local])

