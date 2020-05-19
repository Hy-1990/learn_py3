# -*- coding: UTF-8 -*-
# =================================================
# @Project -> File   ：utils -> __init__.py
# @IDE    ：PyCharm
# @Author ：至尊宝
# @Date   ：2020/5/19 09:14
# @Desc   ：
# ==================================================

# 取质数，else的执行，在于对应for能否顺利执行完成，如果break，则不执行else内内容。
def test_for_else(num):
    for n in range(2, num):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n / x)
                break
        else:
            print(n, 'is a prime number')


if __name__ == '__main__':
    test_for_else(10000)
