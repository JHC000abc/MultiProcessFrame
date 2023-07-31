# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: utils_signal.py
@time: 2023/7/31 18:07
@desc:

"""
from PyQt5.QtCore import pyqtSignal, QObject


class Single(QObject):

    single_int = pyqtSignal(int)
    single_dict = pyqtSignal(dict)
    single_str = pyqtSignal(str)

    def __init__(self):
        super(Single, self).__init__()

    def emit_int(self, msg):
        self.single_int.emit(msg)

    def emit_str(self, msg):
        self.single_str.emit(msg)

    def emit_dict(self, msg):
        self.single_dict.emit(msg)
