import socket

def main():
    HOST = '127.0.0.1'
    PORT = 12345

    # 1. 创建TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 绑定地址和端口
    server_socket.bind((HOST, PORT))
    # 3. 监听连接
    server_socket.listen(5)
    print(f"TCP Server listening on {HOST}:{PORT}")

    while True:
        # 4. 接受客户端连接
        client_socket, client_addr = server_socket.accept()
        print(f"Connected by {client_addr}")

        while True:
            # 5. 接收数据
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode('utf-8')}")
            # 6. 回显数据
            client_socket.sendall(data)

        client_socket.close()

if __name__ == '__main__':
    main()