from flask import Flask, render_template, request, flash, redirect, url_for
from flask_restful import Resource, Api
import requests
import os

app = Flask(__name__)
api = Api(app)
app.secret_key = 'thisisjustarandomstring'

class LessThan(Resource):

    def get(self, number1, number2):
        if(number1 < number2) :
            return {'value' : True}
        else :
            return {'value' : False}

api.add_resource(LessThan, '/LessThan/<int:number1>/<int:number2>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5057,
        host="0.0.0.0"
    )
