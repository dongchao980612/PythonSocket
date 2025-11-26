import socket

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  # 设置5秒的超时时间

    ip="127.0.0.1"

    for port in range(5000,9000):
        result = s.connect_ex((ip,port))
        if result == 0:
            print(f"Port {port} is open")
    
    s.close()