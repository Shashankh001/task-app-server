import socket
import json
from threading import Thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0',2345))
s.listen(100)

def thread(cs):
    argument = cs.recv(1024)
    argument = argument.decode('utf-8')

    if argument == 'LOGIN':
        with open('E:\\Workspace\\Code\\Projects\\Task App - Server Side\\Server\\cred.json', 'r') as f:
            data = f.read()

        cs.send(bytes(data,'utf-8'))
        
        return_code = cs.recv(1024)
        return_code = return_code.decode('utf-8')

        if return_code == 'SUCCESS':
            cs.close()
            print(f'{address} has logged in successfully')


        f.close()
        

    if argument == 'SEND_NOTICE':
        with open('E:\\Workspace\\Code\\Projects\\Task App - Server Side\\Server\\Notices\\data.json','r') as f:
            data = f.read()
            f.close()

        cs.send(bytes(data,'utf-8'))

        data = cs.recv(100000)
        data = data.decode('utf-8')

        data = json.loads(data)

        with open('E:\\Workspace\\Code\\Projects\\Task App - Server Side\\Server\\Notices\\data.json','w') as f:
            json.dump(data, f, indent=4)
            f.close()

        print(f'A notice was sent from {address} successfully')
        cs.close()
            


    if argument == 'SEND_HOMEWORK':
        with open('E:\\Workspace\\Code\\Projects\\Task App - Server Side\\Server\\Homework\\data.json','r') as f:
            data = f.read()
            f.close()

        cs.send(bytes(data,'utf-8'))

        data = cs.recv(100000)
        data = data.decode('utf-8')

        data = json.loads(data)

        with open('E:\\Workspace\\Code\\Projects\\Task App - Server Side\\Server\\Homework\\data.json','w') as f:
            json.dump(data, f, indent=4)
            f.close()

        print(f'Homework was sent from {address} successfully')
        cs.close()

while True:
    cs, address = s.accept()

    t = Thread(target= thread, args = (cs,))
    t.daemon = True
    t.start()