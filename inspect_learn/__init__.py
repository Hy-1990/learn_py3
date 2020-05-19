# -*- coding: UTF-8 -*-
# =================================================
# @Project -> File   ：utils -> __init__.py
# @IDE    ：PyCharm
# @Author ：至尊宝
# @Date   ：2020/5/19 11:23
# @Desc   ：
# ==================================================
import inspect

# 函数自省，判断对象，对象内含有内部方法等
if __name__ == '__main__':
    print(inspect.getmembers(str))
    my_list = [1, 2, 3]
    print(dir(my_list))
    print(type('') is str)
