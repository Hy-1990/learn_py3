# -*- coding: UTF-8 -*-
# =================================================
# @Project -> File   ：utils -> __init__.py
# @IDE    ：PyCharm
# @Author ：至尊宝
# @Date   ：2020/5/19 10:08
# @Desc   ：
# ==================================================
# 增加全局变量，不建议使用
def get_avg(num1, num2):
    global result
    result = num1 + num2


def profile():
    name = "OK"
    age = 10
    return name, age


if __name__ == '__main__':
    get_avg(10, 11)
    print(result)
    print(profile()[0])
