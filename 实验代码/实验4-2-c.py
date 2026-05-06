import socket

def main():
    HOST = '127.0.0.1'
    PORT = 12346

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        msg = input("Input message (or 'quit' to exit): ")
        if msg.lower() == 'quit':
            print("client out...")
            break
        client_socket.sendto(msg.encode('utf-8'), (HOST, PORT))
        data, _ = client_socket.recvfrom(1024)
        print(f"Server reply: {data.decode('utf-8')}")

    client_socket.close()

if __name__ == '__main__':
    main()