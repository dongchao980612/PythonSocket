from MyClassPackage.MyListClass import MyListClass
from MyClassPackage.MyNumClass import MyNumClass

n1 = MyNumClass(10)
print(n1)

n2 = MyNumClass(23)
print(n1 + n2)
print(n1 + 22)
print(20 + n1)


# (n1 + [1])#
# ("e3e"+3)
# print(n1 - n2)
# print(n1 - 22)
# print(20 - n1)




l0 = MyListClass(2)
print(l0)
print(l0, len(l0))
l1 = MyListClass([1, 2, 3])
print(l1, len(l1))
l2 = MyListClass((1, 2, 3, 4))
print(l2, len(l2))
l3 = MyListClass("1234")
print(l3, len(l3))

# print(l1[2])
# l1[1] = 999
# print(l1)


for i in l1:
    print(i)
