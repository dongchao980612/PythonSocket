import socket

from cfg import HOST,PORT

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
# 获取服务器监听的地址
server_addr = server_socket.getsockname()
print("聊天室服务器已启动, 地址: {}:{}, 等待客户端连接...".format(server_addr[0], server_addr[1]))

client_socket, client_addr = server_socket.accept()
print("客户端已连接，地址: {}".format(client_addr))

# 接收客户端消息
data = client_socket.recv(1024).decode()
print("收到客户端消息: {}".format(data))

# 发送响应给客户端
client_socket.send(data.encode())

client_socket.close()
server_socket.close()
