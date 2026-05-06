import os
import time
import sys
from datetime import datetime


class MyLogger:
    """
    自定义日志类
    支持功能：
    1. 日志级别（DEBUG/INFO/WARNING/ERROR/CRITICAL）
    2. 控制台输出 + 文件输出
    3. 日志格式化（时间、级别、模块、内容）
    4. 按文件大小分割日志（避免单文件过大）
    """
    # 定义日志级别（数值越大，级别越高）
    LEVELS = {
        'DEBUG': 10,
        'INFO': 20,
        'WARNING': 30,
        'ERROR': 40,
        'CRITICAL': 50
    }

    def __init__(self,
                 log_dir='logs',  # 日志文件夹
                 log_filename='app.log',  # 日志文件名
                 level='INFO',  # 默认日志级别
                 max_file_size=10 * 1024 * 1024,  # 日志文件最大大小（10MB）
                 backup_count=5):  # 保留的备份日志数量
        # 初始化参数
        self.log_dir = log_dir
        self.log_filename = log_filename
        self.max_file_size = max_file_size
        self.backup_count = backup_count

        # 校验并设置日志级别
        self.level = level.upper()
        if self.level not in self.LEVELS:
            raise ValueError(f"无效的日志级别！可选级别：{list(self.LEVELS.keys())}")
        self.level_value = self.LEVELS[self.level]

        # 创建日志文件夹（不存在则创建）
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        self.log_file_path = os.path.join(self.log_dir, self.log_filename)

    def _check_file_size(self):
        """检查日志文件大小，超过阈值则分割"""
        if not os.path.exists(self.log_file_path):
            return

        # 获取文件大小（字节）
        file_size = os.path.getsize(self.log_file_path)
        if file_size >= self.max_file_size:
            # 重命名原文件为备份文件（如 app.log.1）
            for i in range(self.backup_count - 1, 0, -1):
                src = f"{self.log_file_path}.{i}"
                dst = f"{self.log_file_path}.{i + 1}"
                if os.path.exists(src):
                    if os.path.exists(dst):
                        os.remove(dst)
                    os.rename(src, dst)

            # 重命名当前日志文件为 app.log.1
            if os.path.exists(f"{self.log_file_path}.1"):
                os.remove(f"{self.log_file_path}.1")
            os.rename(self.log_file_path, f"{self.log_file_path}.1")

    def _format_log(self, level, message):
        """格式化日志内容"""
        # 获取当前时间（精确到毫秒）
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

        # 格式化日志行
        log_line = f"[{now}] [{level}] - {message}\n"
        return log_line

    def _write_log(self, level, message):
        """核心写日志方法"""
        # 过滤低于设定级别的日志
        if self.LEVELS[level] < self.level_value:
            return

        # 格式化日志
        log_line = self._format_log(level, message)

        # 1. 输出到控制台（不同级别用不同颜色，可选）
        colors = {
            'DEBUG': '\033[37m',  # 灰色
            'INFO': '\033[32m',  # 绿色
            'WARNING': '\033[33m',  # 黄色
            'ERROR': '\033[31m',  # 红色
            'CRITICAL': '\033[41m'  # 红底白字
        }
        reset_color = '\033[0m'
        # print(f"{colors.get(level, reset_color)}{log_line.strip()}{reset_color}")
        print(f"{log_line.strip()}")

        #  写入文件（先检查文件大小）
        self._check_file_size()
        with open(self.log_file_path, 'a', encoding='utf-8') as f:
            f.write(log_line)

    # 封装各级别日志方法
    def debug(self, message):
        """调试日志"""
        self._write_log('DEBUG', message)

    def info(self, message):
        """信息日志"""
        self._write_log('INFO', message)

    def warning(self, message):
        """警告日志"""
        self._write_log('WARNING', message)

    def error(self, message):
        """错误日志"""
        self._write_log('ERROR', message)

    def critical(self, message):
        """严重错误日志"""
        self._write_log('CRITICAL', message)


# ====================== 测试使用 ======================
if __name__ == "__main__":
    # 1. 创建日志实例（默认级别INFO，日志文件10MB分割，保留5个备份）
    logger = MyLogger(
        log_dir='my_logs',
        log_filename='my_app.log',
        level='DEBUG'  # 设为DEBUG，会输出所有级别日志
    )

    # 2. 测试不同级别日志
    logger.debug("这是调试信息，用于开发调试")
    logger.info("这是普通信息，记录正常流程")
    logger.warning("这是警告信息，需要注意但不影响运行")
    logger.error("这是错误信息，功能执行失败")
    logger.critical("这是严重错误，程序可能崩溃")

    # 3. 结合异常捕获使用
    try:
        1 / 0
    except Exception as e:
        logger.error(f"发生除零错误：{str(e)}")