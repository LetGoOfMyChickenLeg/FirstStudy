#! -*- coding:utf-8 -*-
author = 'lwx468311'

import os

class Joseph:
    def __init__(self, man, sep):
        self.man = man
        self.sep = sep

    def move(self):
        """
        将man列表向左移动sep单位，最左边的元素向列表后面添加
        相当于队列顺时针移动
        """
        for i in range(self.sep):
            # 移除列表中的第一个元素
            item = self.man.pop(0)
            # 把刚刚移除的元素加在列表的最后位置
            self.man.append(item)

    def play(self, rest=2):
        """
        man : people num
        sep : 杀死数到的第几个人
        rest : 幸存者数量
        """
        print("一共{0}个人，每报数到第{1}的人自杀，最后剩余{2}个人".format(self.man, self.sep, rest))
        self.man = [i for i in range(1, self.man + 1)]
        print("玩家队列： {0}".format(self.man))

        self.sep -= 1
        while len(self.man) > rest:
            self.move()
            # 将列表的第一个元素删除
            print("kill", self.man.pop(0))

        return self.man

if __name__ == "__main__":
    Jp = Joseph(41, 3)
    services = Jp.play()
    print("The last live people", services)
