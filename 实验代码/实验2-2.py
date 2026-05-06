# 实验二：流程控制与内置容器
"""
任务二：购物车与订单管理系统
功能：实现商品浏览、购物车管理、订单结算功能
"""

# 商品信息字典（名称、价格、库存）
products = {
    "苹果": {"price": 5.8, "stock": 10},
    "香蕉": {"price": 3.5, "stock": 15},
    "橙子": {"price": 4.2, "stock": 8},
    "牛奶": {"price": 12.0, "stock": 5},
    "面包": {"price": 8.5, "stock": 12}
}

# 购物车列表，每个元素为元组 (商品名称, 单价, 数量)
cart = []

print("=" * 60)
print("欢迎使用购物车系统")
print("=" * 60)

def show_products():
    """显示所有商品"""
    print("\n========== 商品列表 ==========")
    print(f"{'商品名称':<10}{'价格(元)':>10}{'库存':>8}")
    print("-" * 30)
    
    for name, info in products.items():
        print(f"{name:<10}{info['price']:>10.2f}{info['stock']:>8}")
    
    print("-" * 30)

def add_to_cart(name):
    """添加商品到购物车"""

    
    # 检查商品是否存在
    if name not in products:
        print(f"商品“{name}”不存在！")
        return
    
    # 输入数量
    try:
        quantity = int(input("请输入购买数量："))
        if quantity <= 0:
            print("数量必须大于0！")
            return
    except ValueError:
        print("请输入有效的数字！")
        return
    
    # 检查库存
    if quantity > products[name]["stock"]:
        print(f"库存不足！当前库存：{products[name]['stock']}")
        return
    
    # 检查购物车中是否已有该商品
    for i, item in enumerate(cart):
        if item[0] == name:
            # 更新数量
            new_quantity = item[2] + quantity
            if new_quantity > products[name]["stock"]:
                print(f"总数量超出库存！当前库存：{products[name]['stock']}，已有：{item[2]}，最多可加：{products[name]['stock'] - item[2]}")
                return
            # 更新购物车
            cart[i] = (name, products[name]["price"], new_quantity)
            print(f"已更新：{name} x{new_quantity} 到购物车！")
            return
    
    # 添加新商品到购物车
    cart.append((name, products[name]["price"], quantity))
    print(f"已添加：{name} x{quantity} 到购物车！")

def show_cart():
    """查看购物车"""
    if not cart:
        print("\n购物车是空的！")
        return
    
    print("\n========== 购物车内容 ==========")
    print(f"{'序号':<6}{'商品名称':<10}{'单价':>8}{'数量':>6}{'小计':>10}")
    print("-" * 45)
    
    total = 0
    for i, item in enumerate(cart, 1):
        name, price, quantity = item
        subtotal = price * quantity
        total += subtotal
        print(f"{i:<6}{name:<10}{price:>8.2f}{quantity:>6}{subtotal:>10.2f}")
    
    print("-" * 45)
    print(f"{'合计':<24}{'':>8}{'':>6}{total:>10.2f}")
    print("=" * 45)

def modify_cart():
    """修改购物车商品数量"""
    if not cart:
        print("\n购物车是空的，无法修改！")
        return
    
    show_cart()
    
    try:
        index = int(input("\n请输入要修改的商品序号：")) - 1
        if index < 0 or index >= len(cart):
            print("序号无效！")
            return
        
        name, price, current_qty = cart[index]
        print(f"当前商品：{name}，数量：{current_qty}")
        
        new_qty = int(input("请输入新数量（输入0删除该商品）："))
        
        if new_qty < 0:
            print("数量不能为负数！")
            return
        elif new_qty == 0:
            # 删除商品
            del cart[index]
            print(f"已从购物车删除：{name}")
        else:
            # 检查库存
            if new_qty > products[name]["stock"]:
                print(f"库存不足！当前库存：{products[name]['stock']}")
                return
            # 更新数量
            cart[index] = (name, price, new_qty)
            print(f"已修改：{name} 数量改为 {new_qty}")
    
    except ValueError:
        print("请输入有效的数字！")

def remove_from_cart():
    """删除购物车商品"""
    if not cart:
        print("\n购物车是空的，无法删除！")
        return
    
    show_cart()
    
    try:
        index = int(input("\n请输入要删除的商品序号：")) - 1
        if index < 0 or index >= len(cart):
            print("序号无效！")
            return
        
        name = cart[index][0]
        del cart[index]
        print(f"已从购物车删除：{name}")
    
    except ValueError:
        print("请输入有效的数字！")

def checkout():
    """结算生成订单"""
    if not cart:
        print("\n购物车是空的，无法结算！")
        return
    
    print("\n========== 订单结算 ==========")
    print(f"{'商品名称':<10}{'单价':>8}{'数量':>6}{'小计':>10}")
    print("-" * 40)
    
    total = 0
    for item in cart:
        name, price, quantity = item
        subtotal = price * quantity
        total += subtotal
        print(f"{name:<10}{price:>8.2f}{quantity:>6}{subtotal:>10.2f}")
    
    print("-" * 40)
    print(f"{'总计':<24}{total:>10.2f}")
    print("=" * 40)
    
    # 确认结算
    confirm = input("\n确认结算？(y/n)：")
    if confirm.lower() != "y":
        print("已取消结算")
        return
    
    # 更新库存
    for item in cart:
        name, price, quantity = item
        products[name]["stock"] -= quantity
    
    # 清空购物车
    cart.clear()
    print("\n结算成功！感谢您的购买！")

# 主循环
while True:
    print("\n========== 购物车系统 ==========")
    print("1. 显示商品列表")
    print("2. 添加商品到购物车")
    print("3. 查看购物车")
    print("4. 修改购物车商品数量")
    print("5. 删除购物车商品")
    print("6. 结算生成订单")
    print("0. 退出系统")
    print("==================================")
    
    choice = input("请选择操作：")
    
    if choice == "1":
        show_products()
    elif choice == "2":
        print("\n--- 添加商品到购物车 ---")
        name = input("请输入商品名称：")
        add_to_cart(name)
    elif choice == "3":
        show_cart()
    elif choice == "4":
        modify_cart()
    elif choice == "5":
        remove_from_cart()
    elif choice == "6":
        checkout()
    elif choice == "0":
        print("\n感谢使用购物车系统，再见！")
        break
    else:
        print("输入无效，请选择0-7之间的数字！")

print("=" * 60)