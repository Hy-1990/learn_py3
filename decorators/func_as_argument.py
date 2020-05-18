# -*- coding: UTF-8 -*-
# =================================================
# @Project -> File   ：utils -> func_as_argument
# @IDE    ：PyCharm
# @Author ：至尊宝
# @Date   ：2020/5/18 12:09
# @Desc   ：
# ==================================================
def hi():
    def welcome():
        return "hello world!"

    print(welcome())
    return "hi trump!"


def doSomethingBeforeHi(func):
    print("hi sb!")
    print(func())


if __name__ == '__main__':
    greet = hi
    doSomethingBeforeHi(greet)
