from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
import jwt
import hashlib
from pymongo import MongoClient, ReturnDocument

SECRET_KEY = "SPARTA"
from service import userService

import db_connector

db = db_connector.db_connect()

from service.ipService import get_address_from_ip


def start(app, data=''):
    @app.route('/login')
    def getLogin():
        if (request.cookies.get('mytoken')):
            flash("로그인 되어있습니다")
            return redirect(url_for("getUser"))
        else:
            return render_template('login.html')

    @app.route('/user')
    def getUser():
        if (request.cookies.get('mytoken')):
            return render_template('user.html')
        else:
            flash("로그인 하세요")
            return redirect(url_for("getLogin"))

    @app.route('/register')
    def getRegister():
        if (request.cookies.get('mytoken')):
            return redirect(url_for("getUser"))
        else:
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

    @app.route('/getUserInfo', methods=['GET'])
    def getUserInfo():
        token_receive = request.cookies.get('mytoken')
        try:
            # token을 시크릿키로 복호화(디코드)
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
            # payload 안에 id가 존재. 이 id로 해당 user의 닉네임을 찾아냄
            userinfo = db.shelter.find_one({'email': payload['id']}, {'_id': 0})
            userinfo['password'] = ""
            return jsonify({'result': 'success', 'userInfo': userinfo})
        except jwt.ExpiredSignatureError:
            # 위를 실행했는데 만료시간이 지났으면 에러가 납니다.
            return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
        except jwt.exceptions.DecodeError:
            return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})

    @app.route('/postUserInfo', methods=['POST'])
    def postUserInfo():
        try:
            username = request.form['username_receive']
            password = request.form['password_receive']
            address = request.form['address_receive']

            pw_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
            userinfo = db.shelter.find_one_and_update({'email': username, 'password': pw_hash},
                                                      {'$set': {"address": address}},
                                                      {'_id': 0},
                                                      return_document=ReturnDocument.AFTER)
            if userinfo is not None:
                return jsonify({'result': 'success', 'msg': '정보가 변경되었습니다.'})
            else:
                return jsonify({'result': 'fail', 'msg': '비밀번호를 다시 입력해주세요.'})
        except jwt.ExpiredSignatureError:
            return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
        except jwt.exceptions.DecodeError:
            return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})

    @app.route('/getStatus', methods=['GET'])
    def getStatus():
        token_receive = request.cookies.get('mytoken')
        if token_receive is not None:
            return jsonify({'result': 'success', 'bool': True})
        else:
            return jsonify({'result': 'success', 'bool': False})


    @app.route('/updateAddr', methods=['POST'])
    def postUserAddr():
        try:
            address = request.form['address_receive']
            token_receive = request.cookies.get('mytoken')
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
            userinfo = db.shelter.find_one_and_update({'email': payload['id']},
                                                      {'$set': {"address": address}},
                                                      {'_id': 0},
                                                      return_document=ReturnDocument.AFTER)
            print(userinfo)
            if userinfo is not None:
                return jsonify({'result': 'success', 'msg': '정보가 변경되었습니다.'})
            else:
                return jsonify({'result': 'fail'})
        except jwt.ExpiredSignatureError:
            return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
        except jwt.exceptions.DecodeError:
            return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})


