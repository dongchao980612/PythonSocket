class Rectangle:
    def __init__(self, w, h):  # 构造方法，名字是固定的
        self.width = w  # 调用属性的setter方法进行赋值
        self.height = h

    @property
    def width(self):  # 读取属性的值时，自动调用这个方法
        return self.__width

    @width.setter
    def width(self, w):  # 修改属性的值时，自动调用这个方法
        assert isinstance(w, (int, float)) and w > 0, '矩形宽度必须大于0'
        self.__width = w

    @property
    def height(self):  # 读取属性的值时，自动调用这个方法
        return self.__height

    @height.setter
    def height(self, h):  # 修改属性的值时，自动调用这个方法
        if not isinstance(h, (int, float)) or h < 0:
            raise ValueError('矩形高度必须大于0')
        self.__height = h

    @property
    def area(self):
        return self.width * self.height


r1 = Rectangle(3, 5)
print(r1.area)
r2 = Rectangle(4, 6)
r2.width = 9
r2.height = 7
print(r2.area)
