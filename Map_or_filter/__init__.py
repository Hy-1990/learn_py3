# -*- coding: UTF-8 -*-
# =================================================
# @Project -> File   ：utils -> __init__.py
# @IDE    ：PyCharm
# @Author ：至尊宝
# @Date   ：2020/5/19 12:16
# @Desc   ：
# ==================================================
def multiply(x):
    return (x * x)


def add(x):
    return (x + x)


if __name__ == '__main__':
    num_lis = range(-5, 5)
    # ``filter```过滤列表中的元素，并且返回一个由所有符合要求的元素所构成的列表，```符合要求```即函数映射到该元素时返回值为True.
    # 这个```filter```类似于一个```for```循环，但它是一个内置函数，并且更快。
    # 可以取代 for if
    less_lis = filter(lambda x: x < 0, num_lis)
    print(list(less_lis))

    # 大多数时候，我们使用匿名函数(lambdas)来配合`map`, 所以我在上面也是这么做的。
    #  不仅用于一列表的输入， 我们甚至可以用于一列表的函数！
    # `Map`会将一个函数映射到一个输入列表的所有元素上。这是它的规范：
    # 可以取代for set
    items = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x ** 2, items))
    print(squared)
    funcs = [multiply, add]
    for i in range(5):
        value = map(lambda x: x(i), funcs)
        print(list(value))
