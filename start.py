# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: start.py
@time: 2023/7/31 15:14
@desc:

"""
import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt
from qt_material import apply_stylesheet
from gui.ctrl.ctrl_bos import BosMainWindow


if __name__ == "__main__":
    root_path = os.getcwd()
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.path)
    try:
        apply_stylesheet(app, theme="dark_teal.xml")
    except BaseException:
        print("样式加载失败")

    Form = BosMainWindow(root_path)
    Form.show()
    sys.exit(app.exec_())
