# 实验二：流程控制与内置容器
"""
任务一：商品价格查询系统
功能：使用字典存储商品信息，实现查询、显示、添加功能
"""

# 初始化商品字典
products = {
    "苹果": 5.8,
    "香蕉": 3.5,
    "橙子": 4.2,
    "牛奶": 12.0,
    "面包": 8.5
}

print("=" * 50)
print("欢迎使用商品价格查询系统")
print("=" * 50)

# 主循环
while True:
    # 显示菜单
    print("\n========== 商品查询系统 ==========")
    print("1. 查询商品价格")
    print("2. 显示所有商品")
    print("3. 添加新商品")
    print("0. 退出系统")
    print("==================================")

    choice = input("请选择操作：")

    # 1. 查询商品价格
    if choice == "1":
        print("\n--- 查询商品价格 ---")
        name = input("请输入商品名称：")

        if name in products:
            print(f"{name}的价格是：{products[name]:.2f} 元")
        else:
            print(f"商品“{name}”不存在！")

    # 2. 显示所有商品
    elif choice == "2":
        print("\n--- 商品列表 ---")
        print("-" * 30)
        print(f"{'商品名称':<12}{'价格（元）':>12}")
        print("-" * 30)

        for name, price in products.items():
            print(f"{name:<12}{price:>12.2f}")

        print("-" * 30)
        print(f"共有 {len(products)} 种商品")

    # 3. 添加新商品
    elif choice == "3":
        print("\n--- 添加新商品 ---")
        name = input("请输入商品名称：")

        # 检查商品是否已存在
        if name in products:
            overwrite = input(f"商品“{name}”已存在，价格{products[name]:.2f}元，是否覆盖？(y/n)：")
            if overwrite.lower() != "y":
                print("取消添加操作")
                continue

        # 输入价格
        try:
            price = float(input("请输入商品价格："))
            if price < 0:
                print("价格不能为负数！")
                continue
        except ValueError:
            print("价格输入无效，请输入数字！")
            continue

        # 添加商品
        products[name] = price
        print(f"成功添加商品：{name}，价格：{price:.2f}元")

    # 4. 退出系统
    elif choice == "0":
        print("\n感谢使用商品价格查询系统，再见！")
        break

    # 无效输入
    else:
        print("输入无效，请选择1-4之间的数字！")

print("=" * 50)