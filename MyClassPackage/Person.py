class Person:
    def __init__(self, name='', age=30, sex='F'):
        # 初始化私有属性（双下划线）
        self.name = name
        self.age = age
        self.sex = sex

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        # 可选：添加参数校验
        if not isinstance(new_name, str):
            raise ValueError("姓名必须是字符串类型")
        self.__name = new_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):

        if not isinstance(new_age, int) or new_age <= 0:
            raise ValueError("年龄必须是大于0的数值")
        self.__age = new_age

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, new_sex):
        if new_sex not in ('F', 'M'):
            raise ValueError("性别只能是 'F'（女）或 'M'（男）")
        self.__sex = new_sex

    def show(self):
        print("姓名：{}，年龄：{}，性别：{}".format(self.name, self.age, "男" if self.sex == "M" else "女"))


class Teacher(Person):
    def __init__(self, name='', age=30, sex='F',
                 department='Computer'):
        # 调用基类构造方法初始化基类的私有数据成员
        super(Teacher, self).__init__(name, age, sex)
        self.department = department

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, dep):
        if not isinstance(dep, str):
            raise ValueError("字符串类型！")
        self.__department = dep

    def show(self):
        # 先调用父类的同名方法，显示从父类中继承来的数据成员
        super(Teacher, self).show()
        # 再显示派生类中的私有数据成员
        print(self.__department)

    def show_own_attr(self):
        print(self.__department, end="")


# 实现Student类 ，继承于Teacher，添加属性为score
class Student(Teacher):
    def __init__(self, name='', age=30, sex='F',
                 department='Computer', socre=0):
        # 调用基类构造方法初始化基类的私有数据成员
        super(Student, self).__init__(name, age, sex, department)
        self.socre = socre

    @property
    def socre(self):
        return self.__socre

    @socre.setter
    def socre(self, socre):
        if not isinstance(socre, (int, list)):
            raise ValueError("数值类型！")
        self.__socre = socre

    def show_score(self):
        print(self.socre)