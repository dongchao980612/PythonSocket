import os

def create_10gb_file_real(filename="10gb_file_real.bin", chunk_size=1024*1024):
    """真正写入10GB数据"""
    total_size = 10 * 1024 * 1024 * 1024 # 1GB
    chunk = b'\x00' * chunk_size  # 1MB的0
    written = 0
    
    with open(filename, 'wb') as f:
        while written < total_size:
            to_write = min(chunk_size, total_size - written)
            f.write(chunk[:to_write])
            written += to_write
            
            # 显示进度
            if written % (100 * 1024 * 1024) == 0:  # 每100MB
                print(f"已写入: {written / (1024**2):.0f} MB")
    
    actual_size = os.path.getsize(filename)
    print(f"\n完成: {filename}")
    print(f"实际大小: {actual_size / (1024**3):.2f} GB")
if __name__ == '__main__':
    create_10gb_file_real()