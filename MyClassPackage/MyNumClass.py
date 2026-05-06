class MyNumClass:
    def __init__(self, val):
        self.value = val

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        if not isinstance(val, (int, float)):
            raise ValueError("参数必须是数值型")
        self.__value = val

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        if isinstance(other, MyNumClass):
            return self.value + other.value
        elif isinstance(other, (int, float)):
            return self.value + other
        elif isinstance(other, str):
            return "".join([chr(self.value + ord(i)) for i in other])
        else:
            raise ValueError("参数必须是数值型（MyNumClass/int/float）")

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        raise NotImplementedError("请实现函数体")

    def __rsub__(self, other):
        raise NotImplementedError("请实现函数体")


n1 = MyNumClass(2)
print(n1)

n2 = MyNumClass(23)
print(n1 + n2)
print(n1 + 22)
print(20 + n1)
print(n1 + "ab")
list()
# print(n1 - n2)
# print(n1 - 22)
# print(20 - n1)
