import socket
import _thread as thread
import sys

clients = []

def on_new_client(clientsocket,addr):
    while True:
        data = clientsocket.recv(2048)
        print('received {!r}'.format(data))
        if data:
            print('sending data back to the client')
            for client in clients:
                client.sendall(data)
            
        else:
            print('no data from', client_address)
            break
    clientsocket.close()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('127.0.0.1', 65432)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(5)





while True:
   c, addr = sock.accept()     # Establish connection with client.
   print ('Got connection from ', addr)
   clients.append(c)
   thread.start_new_thread(on_new_client,(c,addr))
   #Note it's (addr,) not (addr) because second parameter is a tuple
   #Edit: (c,addr)
   #that's how you pass arguments to functions when creating new threads using thread module.
s.close()
