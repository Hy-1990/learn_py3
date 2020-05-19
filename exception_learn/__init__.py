# -*- coding: UTF-8 -*-
# =================================================
# @Project -> File   ：utils -> __init__.py
# @IDE    ：PyCharm
# @Author ：至尊宝
# @Date   ：2020/5/18 18:32
# @Desc   ：
# ==================================================
# try_catch_else模块中，else是否执行，取决于try部分代码是否产生异常，如异常则else部分不执行，如果不异常则执行。
def test_else():
    try:
        print('hahaha')
        f = open('asdasd', 'rb')
    except Exception:
        print("exception")
    else:
        print('hello')
    finally:
        print('finish!')


if __name__ == '__main__':
    test_else()
