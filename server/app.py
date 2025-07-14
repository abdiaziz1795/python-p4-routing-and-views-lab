#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print string route
@app.route('/print/<string:param>')
def print_string(param):
    print(param)  # Print to console
    return param  # Display in browser

# Count route
@app.route('/count/<int:param>')
def count(param):
    numbers = [f"{i}\n" for i in range(param)]
    return ''.join(numbers)

# Math route
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero."
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation."

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
