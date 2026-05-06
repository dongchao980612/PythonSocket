import socket

from cfg import HOST, PORT

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((HOST, PORT))
    print("成功连接到服务器！")

    # 先发送消息给服务器
    message = input("请输入要发送的消息: ")
    client_socket.send(message.encode())

    # 接收服务器响应
    data = client_socket.recv(1024).decode()
    print("收到服务器消息: {}".format(data))

except Exception as e:
    print("无法连接到服务器！错误: {}".format(e))
finally:
    client_socket.close()
