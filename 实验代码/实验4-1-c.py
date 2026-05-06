import socket

def main():
    HOST = '127.0.0.1'
    PORT = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    while True:
        msg = input("Input message (or 'quit' to exit): ")
        if msg.lower() == 'quit':
            print("client out...")
            break
        client_socket.sendall(msg.encode('utf-8'))
        recv_data = client_socket.recv(1024)
        print(f"Echo from server: {recv_data.decode('utf-8')}")

    client_socket.close()

if __name__ == '__main__':
    main()
