# 新建函数、函数参数、可变对象与不可变对象
def f1(n):
    n = n + 1
    print("f1中n = ", n)


def f2(l):
    l.append(4)
    print("f2中l = ", l)


n = 5
f1(n)
print("f1后n = ", n)

l = [1, 2, 3]
f2(l)
print("f2中l = ", l)

# python中的高级函数
# map
l = ["hello", "world", 'tom']
res = []
for i in l:
    res.append(i.upper())
print(res)

res = list(map(str.upper, l))
print(res)
print(list(map(len, l)))

l = ["hrkjbvie", 6.38, True, None, {"name": "Tom"}]
print(list(map(type, l)))


def say_hi(name):
    return name, ",您好!"


def my_add(a):
    a = a + 1
    return a


names = ['Tom', "jack", 'lili']
print(list(map(say_hi, names)))

# sorted
points = [(3, 4), (5, 7), (5, 6)]


def soretd_by_second_element(item):
    return item[1]


print(list(sorted(points, key=soretd_by_second_element)))

res = {}
s = "hellooeeoollooll"

for i in s:
    if i in res.keys():
        res[i] = res[i] + 1
    else:
        res[i] = 1

print(s)
print(res)


def sorted_by_value(res):
    return res[1]


resed = sorted(res.items(), key=sorted_by_value, reverse=True)
for i in resed[:3]:
    print(i[0])
