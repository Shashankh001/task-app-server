import socket
import json
from threading import Thread
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0',2345))
s.listen(100)

def thread(cs):
    argument = cs.recv(1024).decode('utf-8')
    argument = re.sub(' +', '', argument)
    print(argument)

    if argument == 'LOGIN':
        with open('cred.json', 'r') as f:
            data = f.read()

        cs.send(bytes(data,'utf-8'))
        
        return_code = cs.recv(1024)
        return_code = return_code.decode('utf-8')

        if return_code == 'SUCCESS':
            cs.close()
            print(f'{address} has logged in successfully')

        f.close()

    if argument == 'CLASS_LOGIN':
        with open('classes.json', 'r') as f:
            data = f.read()

        cs.send(bytes(data,'utf-8'))
        
        return_code = cs.recv(1024)
        return_code = return_code.decode('utf-8')

        if return_code == 'SUCCESS':
            cs.close()
            print(f'{address} has logged in successfully')

        f.close()
        

    if argument == 'SEND_NOTICE':
        Class = cs.recv(1024).decode('utf-8')
        Class = re.sub(' +','',Class)

        with open(f'Database/{Class}/Notices/data.json','r') as f:
            data = f.read()
            f.close()

        cs.send(bytes(data,'utf-8'))

        data = cs.recv(100000)
        data = data.decode('utf-8')

        data = json.loads(data)

        with open(f'Database/{Class}/Notices/data.json','w') as f:
            json.dump(data, f, indent=4)
            f.close()

        print(f'A notice was sent from {address} successfully')
        cs.close()
            

    if argument == 'SEND_HOMEWORK':
        Class = cs.recv(1024).decode('utf-8')
        Class = re.sub(' +','',Class)

        with open(f'Database/{Class}/Homework/data.json','r') as f:
            data = f.read()
            f.close()

        cs.send(bytes(data,'utf-8'))

        data = cs.recv(100000)
        data = data.decode('utf-8')

        data = json.loads(data)

        with open(f'Database/{Class}/Homework/data.json','w') as f:
            json.dump(data, f, indent=4)
            f.close()

        print(f'Homework was sent from {address} successfully')
        cs.close()


while True:
    cs, address = s.accept()

    t = Thread(target= thread, args = (cs,))
    t.daemon = True
    t.start()