from flask import Flask, render_template, request, flash, redirect, url_for
from flask_restful import Resource, Api
import requests
import os

app = Flask(__name__)
api = Api(app)
app.secret_key = 'thisisjustarandomstring'

class Multiply(Resource):

    def get(self, number1, number2):
        number3 = number1+number2-1
        return {'value' : number3}


api.add_resource(Multiply, '/Multiply/<int:number1>/<int:number2>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5060,
        host="0.0.0.0"
    )
