from flask import Flask, render_template, request, jsonify

def start(app, data=''):
    @app.route('/', methods=['GET'])
    def home():
        return render_template('index.html')

