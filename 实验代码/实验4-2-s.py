import socket

def main():
    HOST = '127.0.0.1'
    PORT = 12346

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))
    print(f"UDP Server listening on {HOST}:{PORT}")

    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Received from {addr}: {data.decode('utf-8')}")
        reply = f"Server received: {data.decode('utf-8')}"
        server_socket.sendto(reply.encode('utf-8'), addr)

if __name__ == '__main__':
    main()