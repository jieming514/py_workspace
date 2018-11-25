import socket

client = socket.socket()

ip_prot = ("127.0.0.1", 8888)

client.connect(ip_prot)

data = client.recv(1024)
print(data.decode())

while True:
    msg_input = input("please input...")
    client.send(msg_input.encode())
    if msg_input == "exit":

        break
    data = client.recv(1024)
    print(data.decode())
