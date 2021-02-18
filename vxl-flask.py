from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_socketio import SocketIO, emit, disconnect
import socket
import netifaces
from threading import Lock
import random

async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins="*")
thread = None
thread_lock = Lock()

bootstrap = Bootstrap(app)

def get_comms():
  try:
    host_name = socket.gethostname()
    lo_ip = socket.gethostbyname(host_name)
    eth_ip = netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']
    wlan_ip = netifaces.ifaddresses('wlan0')[netifaces.AF_INET][0]['addr']
    print(f'Host name: {host_name} - Eth IP: {eth_ip} - wlan IP: {wlan_ip}')
    return([host_name, lo_ip, eth_ip, wlan_ip])
  except:
    print('Unable to get hostname & IP!')

ws_table = {
    'tableHead' : ['Description', 'Values', 'Units'],
    'tableData' : {
      'rowA':['Filament Voltage', 0, 'V'],
      'rowB':['Filament Current', 0, 'A'],
      'rowC':['Stage Voltage', 0, 'mV'],
      'rowD':['Stage Current', 0, 'uA'],
      'rowE':['Source Voltage', 0, 'kV'],
      'rowF':['Pressure', 0, 'Torr'],
      'rowG':['Lumens', 0, 'V'],
      'rowH':['Temperature', 0, 'C']
      }
    }

def emit_ws_table(polltime = 1):
    print(f'Starting readback polling every { polltime } second.')
    while True:
        socketio.sleep(polltime)
        for i in ws_table['tableData']:
            ws_table['tableData'][i][1] = random.randrange(0, 10)
        socketio.emit('readback_msg', 
            {'data' : ws_table}) #try adding it to namespace='/readbacks' later
        print(f'Readback from rowA: {ws_table["tableData"]["rowA"][0]}: {ws_table["tableData"]["rowA"][1]} {ws_table["tableData"]["rowA"][2]}')  #for validation purposes

def emit_thread():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(emit_ws_table)

@app.route('/')
def index():
  ip_info = get_comms()
  return render_template('index.html', 
    host_name=ip_info[0], lo_ip=ip_info[1], eth_ip=ip_info[2], wlan_ip=ip_info[3])

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
    emit_thread()

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