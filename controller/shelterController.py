from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
from service import shelterService


def start(app, data=''):
    @app.route('/shelter')
    def getShlter():
        myData = shelterService.get_shlter_data(request) # shelter_info
        print(myData)
        return jsonify({'shelter_info': myData})

    @app.route('/current', methods=["GET"])
    def get_current_location():
        current_location_jsonify = shelterService.current_location()
        print(current_location_jsonify)
        return current_location_jsonify

