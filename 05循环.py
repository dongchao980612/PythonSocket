# 使用for循环实现1到n之间所有奇数的和。
# input输入函数
n = int(input())
s = 0
# 方法1
for i in range(1, n+1):
    # 判断
    if i % 2 != 0:
        s = s + i
# 方法2
for i in range(1, n + 1, 2):
    s = s + i
print(s)

# 方法3
l = []
for i in range(1, n + 1, 2):
    l.append(i)

print(sum(l))  # 列表求和

# 列表推导式
s = sum([i for i in range(1, n + 1, 2)])
print(s)

# 计算  1-n之间所有的数的平方和
# n = int(input())
n = 10
s = 0
for i in range(1, n + 1):
    s = s + i ** 2
print(s)

s = sum([i ** 2 for i in range(1, n + 1)])
print(s)

# n=int(input('请输入一个大于0的整数：'))
# 计算1-n的和

# 方法1
n = 5
i, sum = 1, 0  # i和sum分别赋值为1和0
while i<=n: #当i<=n成立时则继续循环，否则退出循环
    sum+=i
    i+=1 #注意该行也是while循环语句序列中的代码，与第4行代码应有相同缩进
print(sum) #输出求和结果


# 方法2
while True:
    if i <= 5:
        sum += i
    else:
        break
    i = i + 1
print(sum)


