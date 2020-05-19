# -*- coding: UTF-8 -*-
# =================================================
# @Project -> File   ：utils -> __init__.py
# @IDE    ：PyCharm
# @Author ：至尊宝
# @Date   ：2020/5/19 09:54
# @Desc   ：
# ==================================================
import time
from functools import lru_cache


# 加入方法缓存，可以大大提升性能，将返回值存在内存，直接使用
@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    start_time = time.time()
    print([fib(n) for n in range(35)])
    print(fib(36))
    end_time = time.time()
    print(end_time - start_time, "s")
