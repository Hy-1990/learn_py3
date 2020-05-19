# -*- coding: UTF-8 -*-
# =================================================
# @Project -> File   ：utils -> __init__.py
# @IDE    ：PyCharm
# @Author ：至尊宝
# @Date   ：2020/5/19 09:36
# @Desc   ：
# ==================================================
# 关键字yield的使用  生成迭代器

def test_generator_func():
    for x in range(100):
        yield x


def fibon(n):
    a = b = 1
    for x in range(n):
        yield a
        a, b = b, a + b


# 凡是带__iter_的对象，都可直接转为迭代器
def test_iterable():
    a = "trump is sb"
    for x in iter(a):
        print(x)


if __name__ == '__main__':
    # for a in test_generator_func():
    #     print(a)
    #
    # for b in fibon(1000):
    #     print(b)
    test_iterable()
