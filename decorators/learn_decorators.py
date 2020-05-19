# -*- coding: UTF-8 -*-
# =================================================
# @Project -> File   ：utils -> learn_decorators
# @IDE    ：PyCharm
# @Author ：至尊宝
# @Date   ：2020/5/18 13:43
# @Desc   ：
# ==================================================
from functools import wraps

# 生成装饰器  @wraps的使用
def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " is running!")
        return func(*args, **kwargs)

    return with_logging


@logit
def test_func(x, y=1000):
    return x + y


if __name__ == '__main__':
    result = test_func(100)
    print(result)
