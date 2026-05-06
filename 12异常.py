try:
    print("hello" + 3)
    # print(3/0)
except TypeError as e:
    print(e)

try:
    print(3 / 0)
except Exception:
    print("err")


def chufa(a, b):
    # assert  b!=0, "b 必须不是0 "
    if b == 0:
        raise ValueError("b 必须不是0")
    return a / b


try:
    chufa(3, 0)
except Exception as e:
    print(e)
