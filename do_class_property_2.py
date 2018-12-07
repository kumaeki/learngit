# -*- coding: utf-8 -*-

class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        self._width =value

    @property
    def heigth(self):
        return self._heigth

    @width.setter
    def height(self,value):
        self._heigth =value

    @property
    def resolution(self):
        return self._width * self._heigth


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
