import socket
import json
import pickle
from threading import Thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0',9876))
s.listen(100)


def thread(cs):
    msg = cs.recv(1024)
    msg = msg.decode('utf-8')

    if msg == 'NOTICE':
        with open('Notices\\data.json','r') as f:
            data = json.load(f)
            f.close()

        jsonString = pickle.dumps(data)
        cs.send(jsonString)
        print(f'[Notice] Sent notice data to {address}')

    if msg == 'HOMEWORK':
        with open('Homework\\data.json','r') as f:
            data = json.load(f)
            f.close()

        jsonString = pickle.dumps(data)
        cs.send(jsonString)
        print(f'[Homework] Sent homework data to {address}')

while True:
    cs, address = s.accept()

    t = Thread(target = thread, args = (cs,))
    t.daemon = True
    t.start()