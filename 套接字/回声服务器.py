import socket
from cfg import HOST, PORT

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)


print("回声服务器已启动，等待客户端连接...")

while True:
    client_socket, client_addr = server_socket.accept()
    print(f"客户端 {client_addr} 已连接")
    while True:
        try:
            # 接收客户端消息
            data = client_socket.recv(1024).decode()
            if not data or data.lower() == 'q':
                print(f"客户端 {client_addr} 已退出")
                break

            client_socket.send(data.encode('utf-8'))
        except Exception :
            client_socket.close()  # 确保关闭客户端连接
            print("客户端连接已关闭")

