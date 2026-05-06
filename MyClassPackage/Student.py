# 定义一个类
class Student:
    """这是一个类"""
    # 定义类成员属性
    name = "Tom"

    def __init__(self, name, age, sex,phone):
        self.m_name = name
        self.m_age = age
        self.m_sex = sex

        self.__m_phone = phone

    @property
    def phone(self):
        return self.__m_phone

    @phone.setter
    def phone(self, phone):
        if len(phone) != 11:
            raise ValueError("手机号必须是11位！")
        self.__m_phone = phone
    def __str__(self):
        return "姓名："+self.name+"年龄:"+str(self.m_age)
    # 定义类成员方法
    def show(self):
        print("This is a student class")


