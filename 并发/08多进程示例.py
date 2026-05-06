import multiprocessing
import shutil
import time
import os

def copy_video(src_file, dst_file):
    print("正在拷贝视频...")
    pid = os.getpid()
    dest_path= dst_file.rsplit("/", 1)[0]
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    begin = time.time()
    shutil.copy(src_file, dst_file)
    cost = time.time() - begin
    size = os.path.getsize(dst_file) / (1024*1024)  # MB
    print(f"[进程{pid}] 完成: {dst_file} ({size:.1f}MB, {cost:.2f}秒)")


if __name__ == '__main__':
    # 配置路径
    src = "./10gb_file_real.bin"      # 源视频
    dst = "./backup/10gb_file_real.bin"    # 目标路径
    begintime = time.time()
    # 单进程拷贝
    # copy_video(src, dst)

    p = multiprocessing.Process(target=copy_video, args=(src, dst))
    p.start()
    p.join()

    print("拷贝完成!")