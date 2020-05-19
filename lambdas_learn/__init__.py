# -*- coding: UTF-8 -*-
# =================================================
# @Project -> File   ：utils -> __init__.py
# @IDE    ：PyCharm
# @Author ：至尊宝
# @Date   ：2020/5/19 11:34
# @Desc   ：
# ==================================================
# lambdas 相当于一个方法体的简化编写方法,匿名函数
def take_second(elem):
    return elem[1]


if __name__ == '__main__':
    add = lambda x, y: x * y
    print(add(100, 9))
    a = [(1, 2), (4, 1), (9, 10), (13, -3)]
    # a.sort(key=lambda x: x[1])
    a.sort(key=take_second)
    print(a)
    b = [1, 2, 3, 4]
    get_2 = lambda x: x > 2
    for x in b:
        print(get_2(x))
    less_than_zero = filter(get_2, b)
    print(list(less_than_zero))
