from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
from service import shelterService


def start(app, data=''):
    @app.route('/api/search/shelter', methods=['GET'])
    def getShlter():
        myData = shelterService.get_shlter_data(request) # shelter_info
        print ('my data is ', myData)
        return jsonify({'shelter_info': myData})

    @app.route('/api/search/shelter/current', methods=["GET"])
    def get_current_location():
        current_location_jsonify = shelterService.current_location()
        return current_location_jsonify

    @app.route('/search', methods=['GET'])
    def getSearch():
        return render_template('search.html')

