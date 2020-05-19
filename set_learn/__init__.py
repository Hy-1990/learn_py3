# -*- coding: UTF-8 -*-
# =================================================
# @Project -> File   ：utils -> __init__.py
# @IDE    ：PyCharm
# @Author ：至尊宝
# @Date   ：2020/5/19 13:56
# @Desc   ：
# ==================================================
# `set`(集合)是一个非常有用的数据结构。它与列表(```list```)的行为类似，区别在于```set```不能包含重复的值。
if __name__ == '__main__':
    lis = ['a', 'b', 'c', 'd', 'a', 'b']
    print(set(lis))
    set_lis = {'a', 'b', 'c'}
    set_lis1 = {'a'}
    print(set_lis.difference(set_lis1))
