from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_socketio import SocketIO, emit
import socket, random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

bootstrap = Bootstrap(app)

def get_host_IP():
  try:
      host_name = socket.gethostname() 
      host_ip = socket.gethostbyname(host_name) 
      print("Hostname :  ",host_name)
      print("IP : ",host_ip)
      return([host_name, host_ip])
  except: 
      print("Unable to get Hostname and IP") 

@app.route('/')
def index():
  ip_info = get_host_IP()
  return render_template('index.html', host_name=ip_info[0], ip_address=ip_info[1])

@app.route('/grafana')
def grafana():
  return render_template('grafana.html')

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

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})
    emit('random number', {'data': int(random.random() * 100)})
    print('Client connected')

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(debug=True)
