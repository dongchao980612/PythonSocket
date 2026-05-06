# 实验一:输入输出与数据类型

"""
任务一：个人信息收集与展示
功能：收集用户个人信息，使用三种方式格式化输出
"""

# 1. 输入部分
name = input("请输入姓名：")
age = int(input("请输入年龄："))
height_cm = int(input("请输入身高（厘米）："))
weight = float(input("请输入体重（千克）："))
is_student_input = input("是否学生（是/否）：")

# 将是否学生转换为布尔值
is_student = is_student_input == "是"

# 2. 计算部分
height_m = height_cm / 100  # 厘米转换为米

# 3. 输出部分
print("\n" + "="*50)

# 方式1：字符串拼接
print("========== 方式1：字符串拼接 ==========")
print("姓名：" + name + "，年龄：" + str(age) + "岁，身高：" + str(height_m) + "米，体重：" + str(weight) + "千克，学生：" + str(is_student))
print("数据类型：姓名：" + str(type(name)) + "，年龄：" + str(type(age)) + "，身高：" + str(type(height_m)) + "，体重：" + str(type(weight)) + "，学生：" + str(type(is_student)))

print("\n" + "="*50)

# 方式2：format方法
print("========== 方式2：format方法 ==========")
print("姓名：{}，年龄：{}岁，身高：{:.2f}米，体重：{:.1f}千克，学生：{}".format(name, age, height_m, weight, is_student))
print("数据类型：姓名：{}，年龄：{}，身高：{}，体重：{}，学生：{}".format(type(name), type(age), type(height_m), type(weight), type(is_student)))

print("\n" + "="*50)

# 方式3：f-string
print("========== 方式3：f-string ==========")
print(f"姓名：{name}，年龄：{age}岁，身高：{height_m:.2f}米，体重：{weight:.1f}千克，学生：{is_student}")
print(f"数据类型：姓名：{type(name)}，年龄：{type(age)}，身高：{type(height_m)}，体重：{type(weight)}，学生：{type(is_student)}")

print("="*50)