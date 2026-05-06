import socket

from cfg import HOST, PORT
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("已连接回声服务器，输入 q 退出\n")

while True:
    msg = input("请输入：")
    if msg.lower() == 'q':
        client_socket.send(msg.encode('utf-8'))
        break

    client_socket.send(msg.encode('utf-8'))
    recv_msg = client_socket.recv(1024).decode('utf-8')
    print(f"服务器回声：{recv_msg}\n")

client_socket.close()
print("已断开连接")