
# 导入模块
import socket

# 创建实例
sk = socket.socket()

# 定义IP和端口
ip_port = ('127.0.0.1', 8888)
sk.bind(ip_port)
# 设置最大监听数
sk.listen(5)

while True:
    print("runing...")
    conn, address = sk.accept()
    msg = "你好"
    conn.send(msg.encode())
    while True:
        data = conn.recv(1024)
        print(data.decode())
        if data == b'exit':
            print("MSG:客户端连接断开...")
            break
        conn.send(data)

    conn.close()
