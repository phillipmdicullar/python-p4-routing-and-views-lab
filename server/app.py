#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route('/')

def index():
    '''Displays a simple welcome message.'''
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:parameter>')
def print_string(parameter):
    '''Displays the provided parameter.'''
    print(parameter)
    return parameter 

@app.route('/count/<int:views>')
def count(views):
    count = '' #initialise an empty string to store the result
    for i in range(views): #loop through the numbers 0 to views -1
        count += f'{i}\n' # append each number followed by a new line 
    return count #return the final string after the loop

    

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    
    elif operation == '-':
        return str(num1 - num2)

    elif operation == '*':
        return str(num1 * num2)

    elif operation == 'div':
        return str(num1 / num2)

    elif operation == '%':
        return str(num1 % num2)

    return 'Operation not recognized. Please use one of the following: + - * div %'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
