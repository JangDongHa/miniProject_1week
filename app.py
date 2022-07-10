from flask import Flask, render_template, request, jsonify

from controller import userController

app = Flask(__name__)

userController.start(app)
# mainController.start(app)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
