from flask import Flask, render_template, request, jsonify

def start(app, data=''):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/search')
    def getSearch():
        return render_template('search.html')