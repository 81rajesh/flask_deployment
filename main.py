# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from flask import Flask,request,render_template,jsonify

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return '<h1> This is the flask application </h1>'

if __name__ == '__main__':
    app.run()