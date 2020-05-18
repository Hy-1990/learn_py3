# -*- coding: UTF-8 -*-
# =================================================
# @Project -> File   ：utils -> __init__.py
# @IDE    ：PyCharm
# @Author ：至尊宝
# @Date   ：2020/4/28 3:22 下午
# @Desc   ：
# ==================================================
import re

if __name__ == '__main__':
    str1 = "[1.3.6.1.2.1.2.1.0 = \"asd\",1.3.6.1.2.1.2.1.0 = a111sd]"
    real_str = re.compile(r'.*=\s*(.*)]')

    print(real_str.findall(str1))

    real_str1 = re.search(r'.*=\s*(.*)]', str1).group()

    print(real_str1)
