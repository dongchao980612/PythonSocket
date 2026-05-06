import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1', 9999))

server_socket.listen(5)

client_socket, client_addr = server_socket.accept()
print("客户端已连接: {}, 地址: {}".format(client_socket, client_addr))

# 接收客户端消息
# data = client_socket.recv(1024)# 字节对象
data = client_socket.recv(1024).decode()  # 字符串

print(type(data))

client_socket.close()
server_socket.close()
