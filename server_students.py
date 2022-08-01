import socket
import json
import pickle
from threading import Thread
import sys
import re
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0',9876))
s.listen(100)

def get_bytesize_string(string, bytelen):
    string_length = sys.getsizeof(string)

    if string_length == bytelen: return None
    
    if string_length < bytelen:
        difference = bytelen - string_length
        for i in range(0, difference):
            string += ' '

        return string

def get_bytesize_bytes(byte, bytelen):
    byte_length = sys.getsizeof(byte)

    if byte_length == bytelen: return None
    
    if byte_length < bytelen:
        difference = bytelen - byte_length
        for i in range(0, difference):
            byte += b' '

        return byte

def thread(cs):
    msg = cs.recv(1024)
    msg = msg.decode('utf-8')
    msg = re.sub(' +', '', msg)
    print(msg)

    if msg == 'NOTICE':
        Class = cs.recv(1024)
        Class = Class.decode('utf-8')
        Class = re.sub(' +', '', Class)

        with open(f'Database/{Class}/Notices/data.json','r') as f:
            data = json.load(f)
            f.close()

        jsonString = pickle.dumps(data)
        cs.send(jsonString)
        print(f'[NOTICE   ] Sent notice data to {address}')

    if msg == 'HOMEWORK':
        Class = cs.recv(1024)
        Class = Class.decode('utf-8')
        Class = re.sub(' +', '', Class)

        with open(f'Database/{Class}/Homework/data.json','r') as f:
            data = json.load(f)
            f.close()

        jsonString = pickle.dumps(data)
        cs.send(jsonString)
        print(f'[HOMEWORK ] Sent homework data to {address}')

while True:
    cs, address = s.accept()

    t = Thread(target = thread, args = (cs,))
    t.daemon = True
    t.start()