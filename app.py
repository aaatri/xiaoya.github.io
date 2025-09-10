# app.py
from flask import Flask, render_template
import os

app = Flask(__name__)

# 设置模板文件夹为当前目录
app.template_folder = '.'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/loading')
def loading():
    return render_template('loading.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)