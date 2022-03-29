from flask import Flask, render_template, request, flash, redirect, url_for
from flask_restful import Resource, Api
import requests
import os

app = Flask(__name__)
api = Api(app)
app.secret_key = 'thisisjustarandomstring'

class Multiply(Resource):

    def get(self, number1, number2):
        
        x = number1
        y = number2
        while(y):
            x,y = y,x%y
        #x is gcd
        
        lcm = number1*number2/x
        
        return {'value' : lcm}


api.add_resource(Multiply, '/Multiply/<int:number1>/<int:number2>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5061,
        host="0.0.0.0"
    )
