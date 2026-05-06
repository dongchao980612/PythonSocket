import socket
import threading

# 配置
from cfg import HOST, PORT


# 处理单个客户端的函数（每个客户端一个线程）
def handle_client(client_socket, client_addr):
    print(f"[新连接] {client_addr} 已上线")

    while True:
        try:
            # 接收客户端消息
            data = client_socket.recv(1024).decode('utf-8')

            # 客户端断开 或 输入q退出
            if not data or data.lower() == 'q':
                print(f"[断开] {client_addr} 已退出")
                break

            # 打印收到的消息
            print(f"[{client_addr}] {data}")


            client_socket.send(data.encode('utf-8'))

        except ConnectionResetError:
            # 客户端强制关闭
            print(f"[异常] {client_addr} 强制断开")
            break

    # 关闭连接
    client_socket.close()


# 主程序
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print("=" * 50)
    print("  多线程回声服务器已启动，等待客户端连接...")
    print(f"  地址: {HOST}:{PORT}")
    print("=" * 50)

    # 循环接收连接
    while True:
        client_socket, client_addr = server_socket.accept()

        # 创建新线程处理这个客户端
        client_thread = threading.Thread(
            target=handle_client,
            args=(client_socket, client_addr)
        )
        client_thread.start()

        # 打印当前活跃线程数（不算主线程）
        print(f"[当前在线] {threading.active_count() - 1} 个客户端")


if __name__ == '__main__':
    main()