from flask import Flask, render_template, request, jsonify

from controller import userController, mainController, weatherController, searchController, shelterController

app = Flask(__name__)
SECRET_KEY = 'SPARTA'
userController.start(app)
mainController.start(app)
weatherController.start(app)
shelterController.start(app)


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run('0.0.0.0', port=5000, debug=True)
