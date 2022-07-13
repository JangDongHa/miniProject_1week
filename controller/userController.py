
from flask import Flask, render_template, jsonify, request, redirect, url_for, flash

from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
import jwt
import hashlib

from pymongo import MongoClient, ReturnDocument

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

    @app.route('/logout')
    def getLogout():
        try:
            mytoken = request.cookies.get('mytoken')
            request.cookies.pop('mytoken')
        except:
            pass

        return render_template('index.html')

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
        userSignupJsonify = userService.user_sign_up(request)
        return userSignupJsonify

    @app.route('/login', methods=['POST'])
    def sign_in():
        userSigninResultJsonify = userService.user_sign_in(request)
        return userSigninResultJsonify

    @app.route('/api/getUserInfo', methods=['GET'])
    def getUserInfo():
        userInfoResultJsonify = userService.user_info(request)
        return userInfoResultJsonify

    @app.route('/api/getStatus', methods=['GET'])
    def getStatus():
        token_receive = request.cookies.get('mytoken')
        print(token_receive)
        if token_receive is not None:
            return jsonify({'result': 'success', 'bool': True})
        else:
            return jsonify({'result': 'success', 'bool': False})


    @app.route('/api/updateAddr', methods=['POST'])
    def postUserAddr():
        changAddrResultJsonify = userService.change_user_addr(request)
        return changAddrResultJsonify

    @app.route('/user/update', methods=['POST'])
    def postUserInfo():
        resultJsonify = userService.user_update(request)
        return resultJsonify

