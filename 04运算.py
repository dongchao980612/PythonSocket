# 数值型运算
print(3 + 6)
print(3 - 8)
print(2 * 87)

print(2 ** 3)  # 幂运算
print(2 ** 100)

print(5 / 2)
print(5 // 2)
print(5.4 / 2.2)
print(5.4 // 2.2)
print(10 % 3)
print(+3)  # 0+3
print(-5)  # 0-5

s1 = "hello"
s2 = "world"
print(s1 + str(6) + s2)
print(s1 * 3)

l1 = [12, 43]
l2 = [432, 54]
print(l1 + l2)
print(l1 * 2)
print("*" * 20)
print("*" * 5)
print("*" * 5)
print("*" * 10)
print("*" * 20)

# 示例
"""
*
**
***
****
"""
for i in range(1, 5):
    print("*" * i)

# 示例
"""
    *
   **
  ***
 ****
*****
"""
for i in range(1, 6):
    print(" " * (6 - i - 1), end="")
    print("*" * i)

# += -= *= /=
a = 10
a = a + 20
a += 20
print(a)

# is操作符
x = 10
y = 10
z = 11
print(x is y, id(x), id(y))

s = "str"
s1 = s
print(s1 is s)

for i in range(6):
    print(i)

# 单分支判断
score=80
if score>=60:
    print("及格!")

# 双分支判断
socre =62
if socre<60:
    print("不及格")
elif socre<70:
    print("及格")

# 多分支判断
s = -2
if s > 5:
    print("ok")
elif s > 0:
    print("ok1")
else:
    print("over...")








names = ["A", "B", "c"]
item = "D"

if item in names:
    print("ok")
else:
    print("error")
