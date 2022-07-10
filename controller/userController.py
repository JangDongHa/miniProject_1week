from flask import Flask, render_template, request, jsonify

from service import userService


def start(app, data=''):
    @app.route('/', methods=['GET']) # '/' must go mainController but define here for test
    def getAll():
        print('1. find users_data to userService in userController (1. userController 가 유저데이터를 찾기 위해 유저서비스를 호출합니다.)')
        users_data = userService.getUsersData()
        print('8. caught users_data from userService in userController (8. userController 가 userService 로부터 정상적으로 유저데이터를 받았습니다.)')
        print('9. jsonify users_data and return to frontend (9. userController 가 frontend로 json 파일을 보내줍니다)')
        return jsonify(users_data=users_data)
