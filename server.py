# from flask import Flask
import time
# app = Flask(__name__)

# @app.route("/")
# def helloworld():
#     return 'hello world'

    ##python decorator functino
    #delay_decorator causes a 2 second pause before running
    #adding @delay_decorator will before defining the function will cause the
    #decorator function to run first followed by the defined function when the defined function is called.
def delay_decorator(function):
    def wrapperfunction():
        time.sleep(2)
        function()
    return wrapperfunction

@delay_decorator
def sayHello():
    print("hello")

@delay_decorator
def saybye():
    print("bye bye bye")

def saygreets():
    print("greets")

sayHello()
saybye()
saygreets()