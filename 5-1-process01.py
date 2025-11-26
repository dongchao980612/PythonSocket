from  multiprocessing import cpu_count
import  subprocess
if __name__ == '__main__':
    # subprocess.run(['pwd'])
    # subprocess.run(['ls', '-l','/'])
    print("CPU 核心数:", cpu_count())