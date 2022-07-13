from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
import jwt
import hashlib
from pymongo import MongoClient

SECRET_KEY="SPARTA"
from service import userService

import db_connector

db = db_connector.db_connect()

from service.ipService import get_address_from_ip


def start(app, data=''):
    def start(app, data=''):
        @app.route('/', methods=['GET'])  # '/' must go mainController but define here for test
        def getAll():
            print(
                '1. find users_data to userService in userController (1. userController 가 유저데이터를 찾기 위해 유저서비스를 호출합니다.)')
            users_data = userService.getUsersData()
            print(
                '8. caught users_data from userService in userController (8. userController 가 userService 로부터 정상적으로 유저데이터를 받았습니다.)')
            print('9. jsonify users_data and return to frontend (9. userController 가 frontend로 json 파일을 보내줍니다)')
            return jsonify(users_data=users_data)

    @app.route('/login')
    def getLogin():
        return render_template('login.html')

    @app.route('/user')
    def getUser():
        return render_template('user.html')

    @app.route('/register')
    def getRegister():
        return render_template('register.html')

    @app.route('/sign_up', methods=['POST'])
    def sign_up():
        username_receive = request.form['username_give']
        password_receive = request.form['password_give']
        email_receive = request.form['email_give']
        address_receive = request.form['address_give']

        password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
        doc = {
            "username": username_receive,  # 아이디
            "password": password_hash,  # 비밀번호
            "email": email_receive,  # 이메일
            "address": address_receive
        }
        db.shelter.insert_one(doc)
        return jsonify({'result': 'success'})

    @app.route('/sign_in', methods=['POST'])
    def sign_in():
        username_receive = request.form['username_give']
        password_receive = request.form['password_give']

        pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
        result = db.shelter.find_one({'email': username_receive, 'password': pw_hash})

        if result is not None:
            payload = {
                'id': username_receive,
                'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

            return jsonify({'result': 'success', 'token': token})
        # 찾지 못하면
        else:
            return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})
