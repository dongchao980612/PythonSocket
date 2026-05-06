class Operator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.res = 0

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):  # 修改属性的值时，自动调用这个方法
        assert isinstance(a, (int, float, list, str)), "a必须是整数或浮点数"
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):  # 修改属性的值时，自动调用这个方法
        assert isinstance(b, (int, float, list, str)), "b必须是整数或浮点数"
        self.__b = b

    def Calculate(self):
        raise NotImplementedError("子类必须实现 Calculate 方法")


class Plus(Operator):
    def __init__(self, a, b):
        super().__init__(a, b)

    def Calculate(self):
        if isinstance(self.a, int) and isinstance(self.b, list):
            return [i+self.a for i in self.b]
        if isinstance(self.a, int) and isinstance(self.b, str):
            return "".join([chr(ord(i) + self.a) for i in self.b])
        return self.a + self.b


class Minus(Operator):
    def __init__(self, a, b):
        super().__init__(a, b)

    def Calculate(self):
        return self.a - self.b


class Multiplication(Operator):
    def __init__(self, a, b):
        super().__init__(a, b)

    def Calculate(self):
        if isinstance(self.a, int) and isinstance(self.b, int) or isinstance(self.a, list) and isinstance(self.b,
                                                                                                          int) or isinstance(
            self.a, str) and isinstance(self.b, int):
            return self.a * self.b
        elif isinstance(self.a, list) and isinstance(self.b, list):
            raise ValueError("不能都是list")
        elif isinstance(self.a, str) and isinstance(self.b, str):
            raise ValueError("不能都是str")


class Division(Operator):
    def __init__(self, a, b):
        super().__init__(a, b)

    def Calculate(self):
        if self.b == 0:
            raise ValueError("不能除0")
        return self.a / self.b


def cal(a, op_str, b):
    # 加法
    if op_str == "+":
        op = Plus(a, b)
        return op.Calculate()

    # 减法
    elif op_str == "-":
        op = Minus(a, b)
        return op.Calculate()

    # 乘法
    elif op_str == "*":
        op = Multiplication(a, b)
        return op.Calculate()

    # 除法
    elif op_str == "/":
        op = Division(a, b)
        return op.Calculate()
    else:
        raise TypeError("不支持的运算")


#
op1 = Plus(1, 2)
print(op1.Calculate())

op2 = Minus(1, 2)
print(op2.Calculate())

op3 = Multiplication(1, 2)
print(op3.Calculate())

op4 = Division(1, 2)
print(op4.Calculate())












# r = cal(3, "+", 6)  # 9
# print(r)
# r = cal(3, "+", 6.6)  # 9.6
# print(r)
# r = cal("hello", "+", "world")  # helloworld
# print(r)
# r = cal([1, 2, 3], "+", [1, 4, 5])  # [1,2,3,1,4,5]
# print(r)
# r = cal(1, "+", [1, 4, 5])  # [2,5,6]
# print(r)
# r = cal(1, "+", "abc")  # bcd
# print(r)

