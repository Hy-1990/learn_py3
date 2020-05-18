# -*- coding: UTF-8 -*-
# =================================================
# @Project -> File   ：utils -> excel_title_sum
# @IDE    ：PyCharm
# @Author ：至尊宝
# @Date   ：2020/4/27 8:14 下午
# @Desc   ：
# ==================================================
import random


def get_title():
    lis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
    first = ''
    cont = 0
    sen = ''
    for i in range(27):
        for j in range(len(lis)):
            if cont == 0:
                sen = sen + lis[j] + "&"
            else:
                sen = sen + first + lis[j] + "&"
        if i != 26:
            first = lis[cont]
        cont = cont + 1
    return sen


def test():
    lis = []
    for i in range(13):
        lis_ci = [x for x in range(random.randint(0, 10))]
        lis.append(lis_ci)
    print(str(lis))


if __name__ == '__main__':
    print(get_title())
    # test()
