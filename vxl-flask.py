from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
  return render_template('index.html')
  return '<h1>Hello World!</h1>'

@app.route('/base')
def base():
  return render_template('base.html')

@app.route('/index_bootstrap')
def index_bootstrap():
  return render_template('index_bootstrap.html')

@app.route('/base_bootstrap')
def base_bootstrap():
  return render_template('base_bootstrap.html')

@app.route('/user/<name>')
def user(name):
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
