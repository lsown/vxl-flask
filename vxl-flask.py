from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_socketio import SocketIO, emit, disconnect
import socket
from threading import Lock
import random

async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins="*")
thread = None
thread_lock = Lock()

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


rb_dict = {
    'tableHead' : ['Description', 'Data', 'Units'],
    'rowA':['Filament Voltage', random.randrange(0,10), 'V'],
    'rowB':['Filament Current', random.randrange(0,10), 'A'],
    'rowC':['Stage Voltage', random.randrange(0,10), 'mV'],
    'rowD':['Stage Current', random.randrange(0,10), 'uA'],
    'rowE':['Source Voltage', random.randrange(0,10), 'kV'],
    'rowF':['Pressure', random.randrange(0,10), 'Torr'],
    'rowG':['Lumens', random.randrange(0,10), 'V'],
    'rowH':['Temperature', random.randrange(0,10), 'C']
    }

def get_readbacks(polltime = 2):
    print(f'Starting readback polling every { polltime } second.')
    while True:
        socketio.sleep(polltime)
        for i in rb_dict:
          if rb_dict[i][2] == 'Data':
            pass
          else:
            rb_dict[i][2] = random.randrange(0, 10)
        socketio.emit('readback_msg', 
            {'data' : rb_dict}) #try adding it to namespace='/readbacks' later
        print(f'Representative readback from rb0: {rb_dict["rowA"][0]}:{rb_dict["rowA"][1]}:{rb_dict["rowA"][2]}')  #for validation purposes

def backMonitor():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(get_readbacks)

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

@app.route('/websockets')
def websockets():
  return render_template('websockets.html')

@app.route('/user/<name>')
def user(name):
  return render_template('index.html')

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})
    #emit('random number', {'data': int(random.random() * 100)})
    #print('Client connected')
    backMonitor()

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.on('test_event')
def test_event():
  print(f'Received a test_event')

@socketio.on('my event')
def my_event(message):
  print(f'Received my event { message }')

@socketio.on('input1_event')
def input1_event(message):
  x = str(message['data'] + ' from input1_event')
  print(f'Received input1 event { x }')
  emit('input1_response', {'data': x})

@socketio.on('input2_event')
def input2_event(message):
  x = message['data']
  print(f'Received input2 event { x }')
  emit('input2_response', {'data': x})

if __name__ == '__main__':
    socketio.run(debug=True)

"""
@app.route('/index_bootstrap')
def index_bootstrap():
  return render_template('index_bootstrap.html')

@app.route('/base_bootstrap')
def base_bootstrap():
  return render_template('base_bootstrap.html')
  """