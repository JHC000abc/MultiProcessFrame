# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: input_output_main_ctrl.py
@time: 2023/7/31 15:11
@desc:

"""
import os
import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from gui.ui.input_output_main import Ui_widget
from threading import Thread
from utils.util_times import TimeProcess



class IOMainWindow(QtWidgets.QWidget):

    """
    输入 输出 标准
    """

    def __init__(self, root_path):
        super(IOMainWindow, self).__init__()
        self.ui = Ui_widget()
        self.ui.setupUi(self)
        self.root_path = root_path
        print(root_path)
        self.__init_ui()
        self.__init_slot()
        self.__init_args()

        self.running_threads = 0

        self.time = TimeProcess()

    def __init_args(self):
        self.input_file = ""
        self.output_file = ""
        self.num_lists = []

        self.nums_msg_map = {}

    def __init_ui(self):
        self.setFixedSize(769, 477)
        # 初始化界面顺序
        self.ui.stackedWidget.setCurrentIndex(0)
        # 初始化按钮样式
        self.ui.pushButton_output.setEnabled(False)
        self.ui.pushButton_sure.setEnabled(False)

    def __init_slot(self):
        # 初始化按钮槽函数
        self.ui.pushButton_help.clicked.connect(
            lambda: QDesktopServices.openUrl(
                QUrl("https://www.baidu.com")))

        self.ui.pushButton_input.clicked.connect(
            lambda: self.select_path(key="入"))
        self.ui.pushButton_output.clicked.connect(
            lambda: self.select_path(key="出"))

        self.ui.pushButton_sure.clicked.connect(self.change_stack_page)

        self.ui.pushButton_num0.clicked.connect(
            lambda: self.number_click(single="0"))
        self.ui.pushButton_num1.clicked.connect(
            lambda: self.number_click(single="1"))
        self.ui.pushButton_num2.clicked.connect(
            lambda: self.number_click(single="2"))
        self.ui.pushButton_num3.clicked.connect(
            lambda: self.number_click(single="3"))
        self.ui.pushButton_num4.clicked.connect(
            lambda: self.number_click(single="4"))
        self.ui.pushButton_num5.clicked.connect(
            lambda: self.number_click(single="5"))
        self.ui.pushButton_num6.clicked.connect(
            lambda: self.number_click(single="6"))
        self.ui.pushButton_num7.clicked.connect(
            lambda: self.number_click(single="7"))
        self.ui.pushButton_num8.clicked.connect(
            lambda: self.number_click(single="8"))
        self.ui.pushButton_num9.clicked.connect(
            lambda: self.number_click(single="9"))

        self.ui.pushButton_yes.clicked.connect(
            lambda: self.number_click(single="Y"))
        self.ui.pushButton_chear.clicked.connect(
            lambda: self.number_click(single="C"))



    def show_single_log(self, msg):
        """

        :param msg:
        :return:
        """
        self.ui.textEdit_logs.append(
            "[{}]-{}\n".format(self.time.get_normal_date(), msg))

    def show_single_dict(self, msg):
        """

        :param msg:
        :return:
        """
        pass

    def show_threads_nums(self, nums):
        """

        :param nums:
        :return:
        """
        self.ui.lcdNumber_thread_nums.display(nums)

    def number_click(self, single):
        """
        拨号
        :param single:
        :return:
        """
        if single == "Y":
            if self.nums_msg_map.get("".join(self.num_lists)) is not None:
                self.change_stack_page()
                t = Thread(
                    target=self.nums_msg_map.get(
                        "".join(
                            self.num_lists))["func"],
                    kwargs={
                        "in_path": self.input_file,
                        "out_path": self.output_file})
                t.start()
            else:
                self.show_mini_win("<font color=red>请对照右侧表格输入正确的ID</font>")
        elif single == "C":
            self.num_lists.clear()
            self.show_lcdNumber(0)
        else:
            if len(self.num_lists) <= 5:
                self.num_lists.append(single)
                self.show_lcdNumber("".join(self.num_lists))
            else:
                self.show_mini_win("拨号过长")

    def show_lcdNumber(self, num):
        """

        :param num:
        :return:
        """
        self.ui.lcdNumber_nums.display(int(num))

    def show_table_tips(self):
        """

        :return:
        """
        num = 0
        model = QtGui.QStandardItemModel()
        # 添加头部
        model.setHorizontalHeaderLabels(["ID", "描述"])
        for id, _map in self.nums_msg_map.items():
            desc = _map["desc"]
            model.appendRow([QtGui.QStandardItem(data) for data in [id, desc]])
            self.ui.tableView_showtips.setModel(model)
            num += 1
        # 最后一行铺满
        self.ui.tableView_showtips.horizontalHeader().setStretchLastSection(True)

    def change_stack_page(self):
        """
        QStackWidget翻页
        :return:
        """
        all_pages = self.ui.stackedWidget.count() - 1
        now_pages = self.ui.stackedWidget.currentIndex()
        next_page = now_pages + 1 if now_pages < all_pages else 0
        self.ui.stackedWidget.setCurrentIndex(next_page)
        if next_page == 1:
            self.show_table_tips()

    def check_input_path(self, path):
        """
        检查输入路径
        :param path:
        :return:
        """
        single = False
        if path:
            if os.path.exists(path):
                if len(os.listdir(path)):
                    single = True
        return single

    def check_output_path(self, path):
        """

        :param path:
        :return:
        """
        single = False
        if path:
            if os.path.exists(path):
                if not len(os.listdir(path)):
                    if self.input_file not in path:
                        single = True
        return single

    def click_nums(self):
        """

        :return:
        """

    def select_path(self, key="入"):
        """

        :param key:
        :return:
        """
        _path = QFileDialog.getExistingDirectory(
            None, "选择输{key}路径".format(key=key))
        # print("_path", _path)
        if key == "入":
            self.input_file = ""
            if self.check_input_path(_path):
                self.ui.lineEdit_input.setPlaceholderText(_path)
                self.input_file = _path
                self.ui.pushButton_output.setEnabled(True)
            else:
                self.ui.lineEdit_input.setPlaceholderText("选择输入路径")
                self.show_mini_win(
                    "<font color=red>请选择正确的输入路径<br>1.输入路径不能为空<br>2.输入路径必须已存在</font>")
        else:
            self.output_file = ""
            if self.check_output_path(_path):
                self.ui.lineEdit_output.setPlaceholderText(_path)
                self.ui.pushButton_sure.setEnabled(True)
                self.output_file = _path
            else:
                self.ui.lineEdit_output.setPlaceholderText("选择输出路径")
                self.show_mini_win(
                    "<font color=red>请选择正确的输出路径<br>1.输出路径不能为空<br>2.输入路径必须为空<br>3.输出路径必须不能包含在输入路径中</font>")

        if self.input_file and self.output_file:
            self.ui.pushButton_sure.setEnabled(True)

    def show_mini_win(self, msg):
        """

        :param msg:
        :return:
        """
        QMessageBox.warning(self, "提示", "{}".format(msg), QMessageBox.Yes)

    def show_two_choice_win(self, msg):
        reply = QMessageBox.question(
            self, "警告", "<font color=red>{}</font>".format(msg))
        if reply == QMessageBox.Yes:
            return True
        else:
            return False

    def closeEvent(self, event) -> None:
        """

        :param event:
        :return:
        """
        running_threads = self.ui.lcdNumber_thread_nums.value()
        if running_threads != 0:
            msg = "当前程序不可结束,等待线程数为0后重试"
        else:
            msg = "点击yes关闭程序"

        flag = self.show_two_choice_win(msg)
        if flag and running_threads == 0:
            event.accept()
            sys.exit(0)
        else:
            event.ignore()
