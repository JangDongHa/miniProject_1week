from flask import Flask, render_template, request, jsonify

from service import userService

from service.ipService import get_address_from_ip


def start(app, data=''):


    @app.route('/login')
    def getLogin():
        return render_template('login.html')

    @app.route('/user')
    def getUser():
        return render_template('user.html')

    @app.route('/register')
    def getRegister():
        return render_template('register.html')
