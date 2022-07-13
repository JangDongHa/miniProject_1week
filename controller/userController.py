from flask import Flask, render_template, request, jsonify

from service import userService

from service.ipService import get_address_from_ip


def start(app, data=''):
    @app.route('/', methods=['GET']) # '/' must go mainController but define here for test
    def getAll():
        get_address_from_ip()
        users_data = userService.getUsersData()
        return jsonify(users_data=users_data)
