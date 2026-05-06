from MyClassPackage.Person import Teacher

t = Teacher(name="李老师", age=35, sex="M", department="数学系")

# # 2. 调用 show 方法展示所有信息
print("=== 初始信息 ===")
t.show()
# # 输出：
# # 姓名：李老师，年龄：35，性别：F
# # 所属部门：Mathematics
#
# # 3. 使用 get 方法获取属性
print("\n=== 获取单个属性 ===")
print("姓名：{}".format(t.name))  # 调用 name 的 get 方法
print("年龄：{}".format(t.age))  # 调用 age 的 get 方法
print("部门：{}".format(t.department))  # 调用 department 的 get 方法
#
# # 4. 使用 set 方法修改属性
print("\n=== 修改属性后 ===")
t.name = "王老师"  # 调用 name 的 set 方法
t.age = 40  # 调用 age 的 set 方法
t.department = "物理系"  # 调用 department 的 set 方法
t.show()

s = Student("sut1",18,"M","yingyu",95)
s.show_score()