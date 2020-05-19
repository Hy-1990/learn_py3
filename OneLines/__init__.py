# -*- coding: UTF-8 -*-
# =================================================
# @Project -> File   ：utils -> __init__.py
# @IDE    ：PyCharm
# @Author ：至尊宝
# @Date   ：2020/5/19 13:23
# @Desc   ：
# ==================================================
import itertools
from pprint import pprint


# 避免类初始化时大量重复的赋值语句
class A(object):
    def __init__(self, a, b, c, d, e, f):
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})


# 您可以通过使用```itertools```包中的```itertools.chain.from_iterable```轻松快速的辗平一个列表。
def change_list(lis):
    return list(itertools.chain.from_iterable(lis))


if __name__ == '__main__':
    my_dict = {'name': 'Yasoob', 'age': 'undefined', 'personality': 'awesome'}
    pprint(my_dict)
    print(my_dict)
    my_list = [[1, 2], [78, 99]]
    print(change_list(my_list))
    lis = []
    dic = {}
    with open('../data/hostname.txt', "r", encoding="utf-8") as f:
        # lis = list(map(lambda x: x.split()[1], f))
        dic.update({x.split()[0]: x.split()[1] for x in f if x is not None and x.split().__len__() == 2})
    print(lis)
    print(dic)
