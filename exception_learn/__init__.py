# -*- coding: UTF-8 -*-
# =================================================
# @Project -> File   ：utils -> __init__.py
# @IDE    ：PyCharm
# @Author ：至尊宝
# @Date   ：2020/5/18 18:32
# @Desc   ：
# ==================================================
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
