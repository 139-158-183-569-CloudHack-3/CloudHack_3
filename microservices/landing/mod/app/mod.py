from flask import Flask, render_template, request, flash, redirect, url_for
from flask_restful import Resource, Api
import requests
import os

app = Flask(__name__)
api = Api(app)
app.secret_key = 'thisisjustarandomstring'

class Modulo(Resource):

    def get(self, number1, number2):
        if(number2 == 0) :
            return {'value' : 'undefined'}
        else :
            return {'value' : number1 % number2}

api.add_resource(Modulo, '/Modulo/<int:number1>/<int:number2>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5055,
        host="0.0.0.0"
    )
