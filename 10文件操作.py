import os
import pickle
import shutil

try:
    os.mkdir("./py_test1")
    # os.mkdir(".\py_test2")
    # os.mkdir(".\ty_test3")
    os.mkdir(".\\py_test4")
except Exception as e:
    print(e)

import os

path = "./mqtt/web"
isExists = os.path.exists(path)
print(isExists)
if isExists:
    print(path + "已经存在！")
else:
    os.makedirs(path)  # 创建递归目录
    print(path + "创建成功！")

# 示例3：删除名为："mqtt/web"的目录
import os

#  加入test.txt
path = "./mqtt/web"  # 空
path1 = "./mqtt/web1"  # 非空
path2 = "./mqtt/web2"  # 空
path3 = "./mqtt/web3"  # 非空

os.rmdir(path)
# os.rmdir(path1) # OSError: [WinError 145] 目录不是空的。: './mqtt/web1'
# shutil.rmtree(path2)
# shutil.rmtree(path3)


#  示例4：复制目录
# import shutil
#
# old_path = "./old_path/old"
# new_path = "./new_path"# 必须不存在
#
# shutil.copytree(old_path, new_path)

import os
import shutil

old_path = "./old_path/old"
new_path = "./new_path"  # 必须不存在
isExits = os.path.exists(new_path)

if isExits:
    shutil.rmtree(new_path)
isExits = os.path.exists(old_path)

if isExits:
    shutil.copytree(old_path, new_path)
else:
    print("目录不存在")
# help(shutil.copytree)

modes = ["r", "w", "a", "r+", "w+", "a+"]

# for index, mode in enumerate(modes):
#     try:
#         f = open("f_{}.txt".format(index + 1), mode)
#     except  Exception as e:
#         print(e, mode)
f = open("./f_2.txt", "r")
data = f.readlines()
print(data)
f.close()


str="Hello Python\n向文件写入数据"
f=open("demo.txt","w",encoding="utf-8")
f.write(str)
f.close()

str="Hello Python\n向文件写入数据1"
f=open("demo.txt","a",encoding="utf-8")
f.write(str)
f.close()

# 以二进制模式写入文件
with open('output.bin', 'wb') as file:
    binary_data = bytes([120, 3, 255, 0, 100])
    file.write(binary_data)

# 以二进制模式读取文件
with open('output.bin', 'rb') as file:
    binary_data = file.read()
    print(list(binary_data))


# 11.py - Python 对象序列化示例



# 序列化：将对象写入文件（二进制模式）
data = {
    "name": "张三",
    "age": 25,
    "scores": [90, 85, 95],
    "is_student": True
}

# 以二进制模式写入（序列化）
with open('data.pkl', 'wb') as f:
    # pickle.dump(待序列化对象, 文件对象)
    pickle.dump(data, f)
print("对象已序列化并保存到 data.pkl")

# 反序列化：从文件读取并恢复对象
f = open('data.pkl', 'rb')
# pickle.load(文件对象)：恢复为原对象
restored_data = pickle.load(f)

print("\n反序列化后的对象：")
print(restored_data)
# 验证类型和内容（和原对象完全一致）
print("类型：{}".format(type(restored_data)))
print("姓名：{}".format(restored_data['name']))
print("分数列表：{}".format(restored_data['scores']))

# serializer.py
import pickle


class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age

    def show_info(self):
        print("用户名：{}，年龄：{}".format(self.username,self.age))


# 序列化并保存
user = User("小红", 22)
with open('user.pkl', 'wb') as f:
    pickle.dump(user, f)


# deserializer.py
import pickle


# 反序列化
with open('user.pkl', 'rb') as f:
    restored_user = pickle.load(f)

restored_user.show_info()  # 输出：用户名：小红，年龄：22

# 读取文件
# with open('test.txt', 'r', encoding='utf-8') as f:
#     content = f.read()
#     print(content)
# 退出with后，文件已自动关闭，无需f.close()

# 写入文件
# with open('test.txt', 'w', encoding='utf-8') as f:
#     f.write('Hello, Python!')
#
# # 二进制模式
# with open('output.bin', 'wb') as f:
#     f.write(bytes([120, 3, 255]))

