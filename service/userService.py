import hashlib

import jwt
from flask import jsonify

from config import token_max_age
from model import usersDao

SECRET_KEY = "SPARTA"

def make_user_info_json(name, password, username, address):
    return {
        "name": name,  # 아이디
        "password": password,  # 비밀번호
        "email": username,  # 이메일
        "address": address
    }

def make_jwt_token(username):
    payload = {
        'id': username,
        'exp': token_max_age  # 로그인 24시간 유지
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def get_jwt_user_info(token_receive):
    # token을 시크릿키로 복호화(디코드)
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    # payload 안에 id가 존재. 이 id로 해당 user의 닉네임을 찾아냄
    userInfo = usersDao.findEmailByUsers(payload['id'])
    userInfo['password'] = ""

    return userInfo

def change_jwt_user_address_info(token_receive, address):

    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    userInfo = usersDao.findOneAndUpdateAddrByusers(payload['id'], address)

    return userInfo

def getUsersData():  # call DAO 잡일 + 모델(CRUD) 요청
    result = usersDao.findUsersByUsers() # list
    return result

def user_sign_up(request):
    username_receive = request.form['name_give']
    password_receive = request.form['password_give']
    email_receive = request.form['username_give'].replace(" ", "")
    address_receive = request.form['address_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    receive_json = make_user_info_json(username_receive, password_hash, email_receive, address_receive)

    if usersDao.findEmailByUsers(email_receive) == False:
        usersDao.insertUsers(receive_json)
        return jsonify({'result': 'success'})
    else:
        return jsonify({'result': 'fail'})

def user_sign_in(request):
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()

    login_result = usersDao.findEmailPasswordByUsers(username_receive, pw_hash)

    if login_result != False: # success
        token = make_jwt_token(username_receive)

        return jsonify({'result': 'success', 'token': token})
    else: #fail
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

def user_info(request):
    token_receive = request.cookies.get('mytoken')
    try:
        userInfo = get_jwt_user_info(token_receive)
        return jsonify({'result': 'success', 'userInfo': userInfo})
    except jwt.ExpiredSignatureError:
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})

def change_user_addr(request):
    try:
        address = request.form['address_receive']
        token_receive = request.cookies.get('mytoken')

        userInfo = change_jwt_user_address_info(token_receive, address)

        if userInfo is not None:
            return jsonify({'result': 'success', 'msg': '정보가 변경되었습니다.'})
        else:
            return jsonify({'result': 'fail'})
    except jwt.ExpiredSignatureError:
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})

def user_update(request):
    try:
        username = request.form['username_receive']
        password = request.form['password_receive']
        address = request.form['address_receive']

        pw_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        userinfo = usersDao.findOneAndUpdateByusers(username, pw_hash, address)
        if userinfo is not None:
            return jsonify({'result': 'success', 'msg': '정보가 변경되었습니다.'})
        else:
            return jsonify({'result': 'fail', 'msg': '비밀번호를 다시 입력해주세요.'})
    except jwt.ExpiredSignatureError:
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})