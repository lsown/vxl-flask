

thread = None
thread_lock = Lock()

def backMonitor():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(aqState)

def aqState():
    while True:
        socketio.sleep(1)
        aqdict['temp'] = aquarium.get_temp()
        aqdict['CleanFlag'] = random.randrange(0,2)
        aqdict['AqFlag'] = random.randrange(0,2)
        aqdict['drv0'] = True if random.randrange(0,2) == 0 else False
        if aqdict['exchangeState'] == True:
            aquarium.drv8825(500, 0, 5000)
            aqdict['exchangeState'] = False
        socketio.emit('aqStatemsg', 
            {'data' : aqdict}, 
            namespace='/aqState')