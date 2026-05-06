# 列表
l = [3, 5, 5.3, "str", 'h', [56, 64], True]
print(l)
print(l[1])
print(l[-2])
print(l[0:3])
l[0] = "new item"
print(l)

print(len(l))
# print(l[len(l)]) error
# print(l.index(999))

# 列表添加
l.append(1561)
l.append("buivr")
l.insert(2, "new data")
print(l)

# 列表删除
# res = l.pop()
l.pop(2)
# print(res)
l.remove(1561)

print(l)


# range函数
print(list(range(10)))

res = sum(list(range(0, 101)))
res1 = sum(list(range(1, 100, 2)))
res2 = sum(list(range(2, 101, 2)))
print(res, res1, res2)

"""
#计算 1-100之内的奇数、偶数、所有数和
s = 0
s1 =0
s2 = 0
for(int i = 0;i<101;i++)
    s = s+i
    if (i%2==0)
        s1=s1+i;
    else    
        s2=s2+i
"""

# 求和函数、最大值函数、最小值函数
l = [2, 3, 54, 54, 76, 8, 76, 434, 64, 54, 76, 43, 7, 43]
print(sum(l), max(l), min(l))

print(l)  # 直接打印

# 遍历
for abc in l:
    print(abc)

# 存在运算符
print(32 in l)



#  元组
t = (2, 3, 4, 5,)
t1 = (2)
print(t)
t2 = (1,)
print(type(t1), type(t2))

lname = ["tom", "jack"]
tname = ("tom", "jack")
print(lname, tname)
lname[0] = "Tom"
# tname[0]="Tom"
H, W = (190, 290)

print(lname, tname)



# 同时遍历两个列表
name = ["A", "B", "c"]
socre = [98, 86, 87]
reslist = []
# 方法一
length = len(name)
for i in list(range(length)):
    reslist.append([name[i], socre[i]])
print(reslist)

# 方法二
reslist = []
for i, j in zip(name, socre):
    reslist.append([i, j])

print(reslist)

m, n, l = 2, 30, 5
print(list(range(m, n, l)))



