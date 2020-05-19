# -*- coding: UTF-8 -*-
# =================================================
# @Project -> File   ：utils -> __init__.py
# @IDE    ：PyCharm
# @Author ：至尊宝
# @Date   ：2020/5/19 13:13
# @Desc   ：
# ==================================================
# 每当你将一个变量赋值为另一个可变类型的变量时，对这个数据的任意改动会同时反映到这两个变量上去。
def add_to_1(elem, target):
    target.append(elem)
    return target


def add_to_2(elem, target=[]):
    target.append(elem)
    return target


# 现在每当你在调用这个函数不传入```target```参数的时候，一个新的列表会被创建
def add_to_3(elem, target=None):
    if target is None:
        target = []
    target.append(elem)
    return target


if __name__ == '__main__':
    lis = []
    print(add_to_1(1, lis))
    print(add_to_1(2, lis))

    print(add_to_2(1))
    print(add_to_2(3))

    print(add_to_3(1))
    print(add_to_3(100))
