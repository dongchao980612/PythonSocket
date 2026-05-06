import pickle

str="Hello Python\n向文件写入数据"

f=open("demo.txt","a",encoding="utf-8")
f.write(str)
f.close()
with open("demo.txt","a",encoding="utf-8") as  abc:
    abc.write(str)
    # abc.close()


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



# 反序列化
with open('user.pkl', 'rb') as f:
    restored_user = pickle.load(f)

restored_user.show_info()  # 输出：用户名：小红，年龄：22
