# 字典
d = {}
# 定义一个字典
d1 = {"name": "Tom", "age": 18, "sex": "M", "score": [87, 89, 91]}

print(d1, d1["name"], d1["age"], d1["sex"], d1["score"])
print(d1.get("name1"))  # 不会报错，没有返回空

print(d1.items())

for k, v in d1.items():
    print("key = ", k, ",v = ", v)

# 获取key
print(d1.keys())

for k in d1.keys():
    print("key = ", k, "value = ", d1[k])

del d1["sex"]  # 删除key
print(d1)


c=dict(zip(['one','two','three'], [1,2,3]))
print(dict(zip(['one','two','three'], [1,2,3])))

name = ["A", "B", "c"]
socre = [98, 86, 87]

print(dict(zip(name,socre)))