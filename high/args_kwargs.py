# -*- coding: UTF-8 -*-
# =================================================
# @Project -> File   ：utils -> args_kwargs
# @IDE    ：PyCharm
# @Author ：至尊宝
# @Date   ：2020/4/28 3:32 下午
# @Desc   ：
# ==================================================

def test_var_args(f_arg, *argv):
    print("常规参数:" + f_arg)
    for arg in argv:
        print("其他参数:" + arg)


def test_var_kwarg(f_arg, **kwargs):
    for key, value in kwargs.items():
        print("{0}:{1}".format(key, value))


class student(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if not hasattr(self, key):
                setattr(self, key, value)

    def __str__(self):
        lis = [attr + ":" + str(self.__dict__[attr]) for attr in self.__dict__]

        print("{", "{0},{1}".format("1", str(lis)), "}")

    def get_score(self, teacher=False):
        if teacher:
            self.score = 100
        else:
            self.score = 0
        self.__str__()


if __name__ == '__main__':
    test_var_args("haha", "a1", "a2", "a3")
    test_var_kwarg("kwarg", name="tuantuan", age=1)
    x = student(name="hy", age=30, score=0)
    print(x.__str__())
    x.get_score(teacher=True)
