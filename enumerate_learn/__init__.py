# -*- coding: UTF-8 -*-
# =================================================
# @Project -> File   ：utils -> __init__.py
# @IDE    ：PyCharm
# @Author ：至尊宝
# @Date   ：2020/5/18 16:15
# @Desc   ：
# ==================================================
# enumerate的使用，可以将列表按照编号开始枚举
def use_enum():
    my_list = ['apple', 'banana', 'grapes', 'pear']
    for c, value in enumerate(my_list, 1):
        print(c, value)
    test_list = list(enumerate(my_list, 100))
    print(test_list)


if __name__ == '__main__':
    use_enum()
