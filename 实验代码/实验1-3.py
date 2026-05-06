# 实验一：输入输出与数据类型
"""
任务三：综合应用 - 月度财务分析系统
功能：个人月度财务分析，计算收支并生成报表
"""

print("="*60)
print("========== 月度财务分析系统 ==========")

# 输入部分
name = input("请输入姓名：")
monthly_salary = int(input("请输入月薪："))
monthly_rent = int(input("请输入每月房租："))
monthly_food = float(input("请输入每月餐饮费用："))
monthly_transport = float(input("请输入每月交通费用："))
work_days = int(input("请输入每月工作天数："))

has_side_income = input("是否有副业收入（是/否）：")
side_income_monthly = 0.0
if has_side_income == "是":
    side_income_monthly = float(input("请输入副业月收入："))
else:
    side_income_monthly = 0.0

print("\n" + "="*60)

# 1. 收入统计
yearly_salary = monthly_salary * 12
yearly_side_income = side_income_monthly * 12
yearly_total_income = yearly_salary + yearly_side_income

print("========== 收入统计 ==========")
print("主业年收入：{:.0f} 元".format(yearly_salary))
if has_side_income == "是":
    print("副业年收入：{:.0f} 元".format(yearly_side_income))
else:
    print("副业年收入：0 元")
print("年总收入：{:.0f} 元".format(yearly_total_income))

print("\n" + "="*60)

# 2. 支出统计
monthly_total_expense = monthly_rent + monthly_food + monthly_transport
yearly_total_expense = monthly_total_expense * 12
expense_ratio = (yearly_total_expense / yearly_total_income) * 100

print("========== 支出统计 ==========")
print("每月总支出：{:.2f} 元".format(monthly_total_expense))
print("年总支出：{:.2f} 元".format(yearly_total_expense))
print("年支出占收入比例：{:.2f}%".format(expense_ratio))

print("\n" + "="*60)

# 3. 结余分析
monthly_balance = monthly_salary - monthly_total_expense + side_income_monthly
yearly_balance = monthly_balance * 12
savings_rate = (yearly_balance / yearly_total_income) * 100

print("========== 结余分析 ==========")
print("每月结余：{:.2f} 元".format(monthly_balance))
print("年结余：{:.2f} 元".format(yearly_balance))
print("结余率：{:.2f}%".format(savings_rate))

print("\n" + "="*60)

# 4. 财务健康评级
print("========== 财务健康评级 ==========")
if savings_rate >= 50:
    rating = "优秀"
elif savings_rate >= 30:
    rating = "良好"
elif savings_rate >= 10:
    rating = "及格"
elif savings_rate >= 0:
    rating = "需改进"
else:
    rating = "危险（入不敷出）"

print("结余率：{:.2f}% → 健康等级：{}".format(savings_rate,rating))

print("\n" + "="*60)

# 5. 详细报表（表格形式）
print("========== 详细报表 ==========")

# 计算各项占比（占月薪的比例）
rent_ratio = (monthly_rent / monthly_salary) * 100
food_ratio = (monthly_food / monthly_salary) * 100
transport_ratio = (monthly_transport / monthly_salary) * 100
balance_ratio = (monthly_balance / monthly_salary) * 100
side_ratio = (side_income_monthly / monthly_salary) * 100

# 打印表头
print("{:<12}{:>12}{:>10}".format('项目', '金额（元）', '占比'))
print("-" * 34)

# 打印各项数据（使用格式化对齐）
print("{:<12}{:>12.2f}{:>10}".format('月薪',monthly_salary,'100.00%'))
if has_side_income == "是":
    print("{:<12}{:>12.2f}{:>9.2f}%".format('副业收入', side_income_monthly, side_ratio))
else:
    print("{:<12}{:>12.2f}{:>10}".format('副业收入', side_income_monthly, '0.00%'))
print("{:<12}{:>12.2f}{:>9.2f}%".format('房租', monthly_rent, rent_ratio))
print("{:<12}{:>12.2f}{:>9.2f}%".format('餐饮', monthly_food, food_ratio))
print("{:<12}{:>12.2f}{:>9.2f}%".format('交通', monthly_transport, transport_ratio))
print("-" * 34)
print("{:<12}{:>12.2f}{:>9.2f}%".format('月结余', monthly_balance, balance_ratio))

print("="*60)

# 额外提示信息（根据健康等级给出建议）
print("\n【财务建议】")
if rating == "优秀":
    print("恭喜！您的财务健康状况优秀，可以考虑投资理财，让钱生钱。")
elif rating == "良好":
    print("财务状况良好，建议继续保持，适当增加储蓄。")
elif rating == "及格":
    print("财务状况基本健康，建议优化支出结构，提高储蓄率。")
elif rating == "需改进":
    print("储蓄率偏低，建议控制非必要支出，增加收入来源。")
else:
    print("财务状况需要紧急改善，建议重新评估收支，减少负债。")

print("\n" + "="*60)