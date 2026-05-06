class MyListClass:
    def __init__(self, val):
        self.value = val

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        if isinstance(val, (list, tuple, str)):
            self.__value = list(val)
        elif isinstance(val, (int, float)):
            self.__value = val
        else:
            raise TypeError("仅支持 list/tuple/str/int/float 类型")

    def __str__(self):
        return "数据值是："+str(self.value)

    def __len__(self):

        if isinstance(self.value, (float, list, tuple, str, MyListClass)):
            return len(self.value)
        elif isinstance(self.value, (int)):
            return 1
        else:
            raise TypeError("类型不支持获取长度")

    def __getitem__(self, index):
        if isinstance(self.value, (float, list, tuple, str)) and index > len(self.value):
            raise Exception("下标越界")
        elif isinstance(self.value, (int)):
            raise TypeError("数值类型（int/float）不可以索引")
        return self.value[index]

    def __setitem__(self, index, value):
        if not isinstance(value, int):
            raise TypeError("索引必须是整数类型")

        if isinstance(self.value, (float, list, tuple, str)) and index > len(self.value):
            raise Exception("下标越界")
        elif isinstance(self.value, (int)):
            raise TypeError("数值类型（int/float）不支持索引赋值")

        # 5. 执行赋值操作
        self.value[index] = value



