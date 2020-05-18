# -*- coding: UTF-8 -*-
# =================================================
# @Project -> File   ：utils -> return_func_in_func
# @IDE    ：PyCharm
# @Author ：至尊宝
# @Date   ：2020/5/18 13:59
# @Desc   ：
# ==================================================
def res_to_str(context):
    def str_get():
        return context

    def lis_get():
        result = ""
        for x in context:
            result = result + str(x) + ","
        return result

    if context is str:
        return str_get()
    elif type(context) is list:
        return lis_get()
    else:
        return str(context)


if __name__ == '__main__':
    lis_test = ['a', 'b', 1]
    dic_test = {"a": 100}
    print(type(lis_test) is list)
    print(res_to_str("asd"))
