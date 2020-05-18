# -*- coding: UTF-8 -*-
# =================================================
# @Project -> File   ：utils -> bean
# @IDE    ：PyCharm
# @Author ：至尊宝
# @Date   ：2020/4/27 12:00 下午
# @Desc   ：
# ==================================================

class Excel_Sheet:
    sheet_names = ""
    cells = {}

    def __init__(self, sheet_names, cells):
        self.sheet_names = sheet_names
        self.cells = cells

    def set_sheet_names(self, name):
        self.sheet_names = name

    def shet_cells(self, cells):
        self.cells = cells

    def get_sheet_names(self):
        return self.sheet_names

    def get_cells(self):
        return self.cells
