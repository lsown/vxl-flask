from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_socketio import SocketIO, emit
import socket
from threading import Lock
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

bootstrap = Bootstrap(app)

thread = None
thread_lock = Lock()

def get_host_IP():
  try:
      host_name = socket.gethostname() 
      host_ip = socket.gethostbyname(host_name) 
      print("Hostname :  ",host_name)
      print("IP : ",host_ip)
      return([host_name, host_ip])
  except: 
      print("Unable to get Hostname and IP") 


rb_dict = {
    'rb0': random.randrange(0,10),
    'rb1' : True if random.randrange(0,2) == 0 else False,
    'rb2' : True if random.randrange(0,2) == 0 else False,
    'rb3' : random.randrange(0,1),
    'rb4' : random.randrange(0,10),
    'rb5' : random.randrange(0,100),
    'rb6' : random.randrange(0,1000),
    'rb7' : random.randrange(0,10000),
    }

def get_readbacks(polltime = 1):
    print(f'Starting readback polling every { polltime } second.')
    while True:
        socketio.sleep(polltime)
        for i in rb_dict:
          rb_dict[i] = random.randrange(0, 10)
        socketio.emit('readback_msg', 
            {'data' : rb_dict}, 
            namespace='/readbacks')
        print(rb_dict['rb0'])

def backMonitor():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(get_readbacks)

def ack():
    print 'message was received!'

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
    backMonitor()

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.on('test_event')
def test_event():
  print(f'Received a test_event')

if __name__ == '__main__':
    socketio.run(debug=True)
