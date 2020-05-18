# -*- coding: UTF-8 -*-
# =================================================
# @Project -> File   ：utils -> deque_test
# @IDE    ：PyCharm
# @Author ：至尊宝
# @Date   ：2020/4/29 10:35 上午
# @Desc   ：
# ==================================================
from collections import deque
from collections import namedtuple
from enum import Enum


class Species(Enum):
    cat = 1
    dog = 2
    horse = 3

    # 但我们并不想关心同一物种的年龄，所以我们可以使用一个别名
    kitten = 1  # (译者注：幼小的猫咪)
    puppy = 2  # (译者注：幼小的狗狗)


def get_deque():
    lis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
    # 双向队列 设置最大长度
    d = deque(maxlen=10)
    for x in lis:
        d.append(x)
    print(d)
    d.extendleft([1])
    print(d)
    d.extend(["trump", "is", "SB"])
    print(d)

    Animal = namedtuple('Animal', 'name age type')
    cherry = Animal(name="trump", age=78, type=Species.dog)
    print(cherry.name)
    cherry._replace(age=109)
    print(cherry._asdict())


if __name__ == '__main__':
    get_deque()
