from flask import Flask, render_template, request, flash, redirect, url_for
from flask_restful import Resource, Api
import requests
import os

app = Flask(__name__)
api = Api(app)
app.secret_key = 'thisisjustarandomstring'

""" class Add(Resource):

    def get(self, number1, number2):
        return number1 + number2

class Subtract(Resource):

    def get(self, number1, number2):
        return number1 - number2

class Multiply(Resource):

    def get(self, number1, number2):
        return number1 * number2

class Divide(Resource):

    def get(self, number1, number2):
        if(number2 == 0) :
            return 'undefined';
        else :
            return number1 / number2


def add(n1, n2):
    return n1+n2

def minus(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

api.add_resource(Add, '/Add/<int:number1>/<int:number2>')
api.add_resource(Subtract, '/Subtract/<int:number1>/<int:number2>')
api.add_resource(Multiply, '/Multiply/<int:number1>/<int:number2>')
api.add_resource(Divide, '/Divide/<int:number1>/<int:number2>')
"""

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index():
    try :
        number_1 = int(request.form.get("first"))
        number_2 = int(request.form.get('second'))
    except:
        flash(f'Please enter valid value')
        return render_template('index.html')
    operation = request.form.get('operation')
    result = 0
    if operation == 'add':
        url = f'http://addition-service:5051/Add/{number_1}/{number_2}'
        result = requests.get(url).json()['value']
        print(result)
    elif operation == 'minus':
        url = f'http://subtraction-service:5052/Subtract/{number_1}/{number_2}'
        result = requests.get(url).json()['value']
    elif operation == 'multiply':
        url = f'http://multiplication-service:5053/Multiply/{number_1}/{number_2}'
        result = requests.get(url).json()['value']
    elif operation == 'divide':
        url = f'http://division-service:5054/Divide/{number_1}/{number_2}'
        result = requests.get(url).json()['value']

    flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
