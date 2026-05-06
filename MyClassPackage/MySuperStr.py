class MySuperStr(str):

    def __add__(self, other):
        if isinstance(other, int):
            return self + str(other)
        return self+other

s = MySuperStr("hello")
print(s + "hh")
