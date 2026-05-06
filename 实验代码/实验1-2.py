# 实验一：输入输出与数据类型

"""
任务二：数据类型与运算探索
功能：类型转换实验、算术运算计算器、字符串魔法
"""

print("="*60)
print("========== 类型转换实验 ==========")

# 1. 整数转浮点数
num_int = 99
num_float = float(num_int)
print(f"{num_int} -> {num_float} (类型：{type(num_float)})")

# 2. 浮点数转整数
pi = 3.14159
pi_int = int(pi)
print(f"{pi} -> {pi_int} (类型：{type(pi_int)})")

# 3. 字符串转整数
str_num1 = "2024"
int_num1 = int(str_num1)
print(f'"{str_num1}" -> {int_num1} (类型：{type(int_num1)})')

# 4. 字符串转浮点数
str_num2 = "98.6"
float_num = float(str_num2)
print(f'"{str_num2}" -> {float_num} (类型：{type(float_num)})')

# 5. 整数转布尔值
zero = 0
bool_zero = bool(zero)
print(f"{zero} -> {bool_zero} (类型：{type(bool_zero)})")

five = 5
bool_five = bool(five)
print(f"{five} -> {bool_five} (类型：{type(bool_five)})")

# 6. 字符串转布尔值
str_false = "False"
bool_str_false = bool(str_false)
print(f'"{str_false}" -> {bool_str_false} (类型：{type(bool_str_false)})')

print("\n" + "="*60)
print("========== 算术运算计算器 ==========")

# 算术运算计算器
num1 = float(input("请输入第一个数字："))
num2 = float(input("请输入第二个数字："))

print(f"\n{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} × {num2} = {num1 * num2}")
print(f"{num1} ÷ {num2} = {num1 / num2:.2f}")  # 保留两位小数
print(f"{num1} ÷ {num2} 的整数部分 = {num1 // num2}")
print(f"{num1} ÷ {num2} 的余数 = {num1 % num2}")
print(f"{num1} 的 {num2} 次方 = {num1 ** num2}")

print("\n" + "="*60)
print("========== 字符串魔法 ==========")

# 字符串魔法
str1 = input("请输入第一个字符串：")
str2 = input("请输入第二个字符串：")

# 字符串拼接
concat_str = str1 + str2
print(f"拼接结果：{concat_str}")

# 字符串重复
repeat_str = str1 * 3
print(f"重复3次：{repeat_str}")

# 字符串长度
len1 = len(str1)
len2 = len(str2)
print(f"第一个字符串长度：{len1}，第二个字符串长度：{len2}")

# 第一个字符和最后一个字符
first_char = str1[0]
last_char = str1[-1]
print(f"第一个字符：{first_char}，最后一个字符：{last_char}")

print("="*60)