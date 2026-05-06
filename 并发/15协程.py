import asyncio
import time

# 定义协程函数
async def sing():
    for i in range(3):
        print("唱歌中...")
        await asyncio.sleep(1)  # 模拟I/O操作（非阻塞）
# 定义协程函数
async def dance():
    for i in range(3):
        print("跳舞中...")
        await asyncio.sleep(1)  # 模拟I/O操作（非阻塞）

# 运行协程的主函数
async def main():
    begintime = time.time()
    await asyncio.gather(
        sing(),
        dance()
    )

    endtime = time.time()
    print("总用时: {}".format(endtime - begintime))
    
if __name__ == "__main__":
    asyncio.run(main())