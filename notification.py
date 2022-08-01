import socket
from threading import Thread

user_list = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0',7489))
s.listen(100)


def main(cs):
    arg = cs.recv(1024).decode('utf-8')

    if arg == 'HOMEWORK':
        for i in range(0, len(user_list)):
            new_socket = user_list[i]
            new_socket.send(bytes(''))
while True:
    cs, address = s.accept()
    
    user_list.append(cs)

    t = Thread(target=main, args=(cs,))
    t.daemon = True
    t.start()