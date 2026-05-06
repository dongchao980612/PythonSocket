# 变量地址
x = 3
print(x)
print(id(x))

x = "hello"
print(x)
print(id(x))

y = x
print(y)
print(id(y))


# 标识符
PI = 3.14
abc = 10
# 1uirwebj=91
lujing = "vbnm,."
# lu jing  = ""
lu_jing = "vbunil"
Lu_jing = ""
# lu_@_bue="bn"

# 多变量初始化
x, y = 10, 20
print(x)
print(y)

name, age = '张三', 18
print(name)
print(age)

x = 10
y = 20
y, x = x, y
print(x, y)


# 数值型
b_num = 0b1
o_num = 0o6
num = 12
d_num = 0x3d
print(b_num, o_num, num, d_num)
print(bin(num), oct(num), hex(num))

# 浮点型
print(0.4-0.3==0.1)# False

G = 6.74e-11
print(G)


# 字符串
s1 = "abc"
s2 = 'abc'
s3 = """abc"""
s4 = '''abc'''

# "  i say "2vuu" ,ahah  "
"  i say 'hahah' ,hahh  "
print(type(s3))


# 类型转换
print(int("1986"), type("1986"), type(int("1986")))
print("3.14", float("3.14"))



# 字符串切片
s = "helloworld,bvfidu ,hewn"
print(s[10:15])

number = "223500121"
print(number[6:9])
print(number[-3:])

# 获取35
print(number[2:4])
print(number[-7:-5])


# 切片示例
id_str = "220123200002121358"

year = id_str[6:10]
month = id_str[10:12]
age = 2026 - int(year)

print("年份", year)
print("月份", month)
print("age", age)
