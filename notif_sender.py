import socket



def send(arg, message): #usage: send("HW","The notification message")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.0.102',2222))

    s.send(bytes(arg,'utf-8'))

    message = f"{message[:30]}..."
    s.send(bytes(message,'utf-8'))