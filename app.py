from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World! :)<h1>'

# @app.route('/greet')
# def greet():
#     return 'Hello'


@app.route('/greet/<name>')
def greet(name=""):
    return 'Hello {}'.format(name)


def celsius_to_fahrenheit(value):
    f = (value * 9/5) + 32
    return f


@app.route('/f')
@app.route('/f/<value>')
def f(value=0):
    number = float(value)
    result = celsius_to_fahrenheit(number)
    return "Input Value = {} Result = {}".format(value, result)


if __name__ == '__main__':
    app.run()
