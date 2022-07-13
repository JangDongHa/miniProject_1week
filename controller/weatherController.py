from flask import Flask, render_template, request, jsonify
from service import userService, ipService


def start(app, data=''):
    @app.route('/api/weather', methods=['GET'])  # '/' must go mainController but define here for test
    def get_api_weather():
        address = request.args.get('address')
        users_data = userService.getUsersData()
        return jsonify(users_data=users_data)

    @app.route('/api/tempAddress', methods=['GET'])
    def get_temp_address():
        return ipService.get_address_from_ip()

    @app.route('/weather', methods=['GET'])
    def get_weather():
        return render_template('weather.html')