# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input_output_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(769, 477)
        self.stackedWidget = QtWidgets.QStackedWidget(widget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 0, 751, 471))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton_input = QtWidgets.QPushButton(self.page)
        self.pushButton_input.setGeometry(QtCore.QRect(592, 140, 91, 41))
        self.pushButton_input.setObjectName("pushButton_input")
        self.lineEdit_input = QtWidgets.QLineEdit(self.page)
        self.lineEdit_input.setGeometry(QtCore.QRect(60, 140, 501, 41))
        self.lineEdit_input.setObjectName("lineEdit_input")
        self.lineEdit_output = QtWidgets.QLineEdit(self.page)
        self.lineEdit_output.setGeometry(QtCore.QRect(60, 200, 501, 41))
        self.lineEdit_output.setObjectName("lineEdit_output")
        self.label_title = QtWidgets.QLabel(self.page)
        self.label_title.setGeometry(QtCore.QRect(250, -10, 231, 101))
        self.label_title.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 18pt \"黑体\";\n"
"border: 2px solid black;\n"
"\n"
"border-top: none;\n"
"border-left: none;\n"
"border-right: none;\n"
"margin-top:50px;")
        self.label_title.setObjectName("label_title")
        self.pushButton_output = QtWidgets.QPushButton(self.page)
        self.pushButton_output.setGeometry(QtCore.QRect(590, 200, 91, 41))
        self.pushButton_output.setObjectName("pushButton_output")
        self.pushButton_help = QtWidgets.QPushButton(self.page)
        self.pushButton_help.setGeometry(QtCore.QRect(590, 50, 93, 41))
        self.pushButton_help.setObjectName("pushButton_help")
        self.pushButton_sure = QtWidgets.QPushButton(self.page)
        self.pushButton_sure.setGeometry(QtCore.QRect(510, 270, 171, 41))
        self.pushButton_sure.setObjectName("pushButton_sure")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.frame = QtWidgets.QFrame(self.page_2)
        self.frame.setGeometry(QtCore.QRect(30, 190, 291, 271))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_num7 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_num7.sizePolicy().hasHeightForWidth())
        self.pushButton_num7.setSizePolicy(sizePolicy)
        self.pushButton_num7.setObjectName("pushButton_num7")
        self.gridLayout.addWidget(self.pushButton_num7, 0, 0, 1, 1)
        self.pushButton_num8 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_num8.sizePolicy().hasHeightForWidth())
        self.pushButton_num8.setSizePolicy(sizePolicy)
        self.pushButton_num8.setObjectName("pushButton_num8")
        self.gridLayout.addWidget(self.pushButton_num8, 0, 1, 1, 1)
        self.pushButton_num9 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_num9.sizePolicy().hasHeightForWidth())
        self.pushButton_num9.setSizePolicy(sizePolicy)
        self.pushButton_num9.setObjectName("pushButton_num9")
        self.gridLayout.addWidget(self.pushButton_num9, 0, 2, 1, 1)
        self.pushButton_num4 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_num4.sizePolicy().hasHeightForWidth())
        self.pushButton_num4.setSizePolicy(sizePolicy)
        self.pushButton_num4.setObjectName("pushButton_num4")
        self.gridLayout.addWidget(self.pushButton_num4, 1, 0, 1, 1)
        self.pushButton_num5 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_num5.sizePolicy().hasHeightForWidth())
        self.pushButton_num5.setSizePolicy(sizePolicy)
        self.pushButton_num5.setObjectName("pushButton_num5")
        self.gridLayout.addWidget(self.pushButton_num5, 1, 1, 1, 1)
        self.pushButton_num6 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_num6.sizePolicy().hasHeightForWidth())
        self.pushButton_num6.setSizePolicy(sizePolicy)
        self.pushButton_num6.setObjectName("pushButton_num6")
        self.gridLayout.addWidget(self.pushButton_num6, 1, 2, 1, 1)
        self.pushButton_num1 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_num1.sizePolicy().hasHeightForWidth())
        self.pushButton_num1.setSizePolicy(sizePolicy)
        self.pushButton_num1.setObjectName("pushButton_num1")
        self.gridLayout.addWidget(self.pushButton_num1, 2, 0, 1, 1)
        self.pushButton_num2 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_num2.sizePolicy().hasHeightForWidth())
        self.pushButton_num2.setSizePolicy(sizePolicy)
        self.pushButton_num2.setObjectName("pushButton_num2")
        self.gridLayout.addWidget(self.pushButton_num2, 2, 1, 1, 1)
        self.pushButton_num3 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_num3.sizePolicy().hasHeightForWidth())
        self.pushButton_num3.setSizePolicy(sizePolicy)
        self.pushButton_num3.setObjectName("pushButton_num3")
        self.gridLayout.addWidget(self.pushButton_num3, 2, 2, 1, 1)
        self.pushButton_chear = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_chear.sizePolicy().hasHeightForWidth())
        self.pushButton_chear.setSizePolicy(sizePolicy)
        self.pushButton_chear.setObjectName("pushButton_chear")
        self.gridLayout.addWidget(self.pushButton_chear, 3, 0, 1, 1)
        self.pushButton_num0 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_num0.sizePolicy().hasHeightForWidth())
        self.pushButton_num0.setSizePolicy(sizePolicy)
        self.pushButton_num0.setObjectName("pushButton_num0")
        self.gridLayout.addWidget(self.pushButton_num0, 3, 1, 1, 1)
        self.pushButton_yes = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_yes.sizePolicy().hasHeightForWidth())
        self.pushButton_yes.setSizePolicy(sizePolicy)
        self.pushButton_yes.setObjectName("pushButton_yes")
        self.gridLayout.addWidget(self.pushButton_yes, 3, 2, 1, 1)
        self.tableView_showtips = QtWidgets.QTableView(self.page_2)
        self.tableView_showtips.setGeometry(QtCore.QRect(325, 21, 421, 441))
        self.tableView_showtips.setObjectName("tableView_showtips")
        self.label_nums = QtWidgets.QLabel(self.page_2)
        self.label_nums.setGeometry(QtCore.QRect(70, -20, 181, 91))
        self.label_nums.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 18pt \"黑体\";\n"
"border: 2px solid black;\n"
"\n"
"border-top: none;\n"
"border-left: none;\n"
"border-right: none;\n"
"margin-top:50px;")
        self.label_nums.setObjectName("label_nums")
        self.lcdNumber_nums = QtWidgets.QLCDNumber(self.page_2)
        self.lcdNumber_nums.setGeometry(QtCore.QRect(43, 102, 271, 71))
        self.lcdNumber_nums.setObjectName("lcdNumber_nums")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.lcdNumber_thread_nums = QtWidgets.QLCDNumber(self.page_3)
        self.lcdNumber_thread_nums.setGeometry(QtCore.QRect(570, 20, 171, 71))
        self.lcdNumber_thread_nums.setObjectName("lcdNumber_thread_nums")
        self.textEdit_logs = QtWidgets.QTextEdit(self.page_3)
        self.textEdit_logs.setGeometry(QtCore.QRect(10, 120, 741, 341))
        self.textEdit_logs.setObjectName("textEdit_logs")
        self.label_logs = QtWidgets.QLabel(self.page_3)
        self.label_logs.setGeometry(QtCore.QRect(260, 0, 181, 91))
        self.label_logs.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 18pt \"黑体\";\n"
"border: 2px solid black;\n"
"\n"
"border-top: none;\n"
"border-left: none;\n"
"border-right: none;\n"
"margin-top:50px;")
        self.label_logs.setObjectName("label_logs")
        self.stackedWidget.addWidget(self.page_3)

        self.retranslateUi(widget)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "采集批处理工具集"))
        self.pushButton_input.setToolTip(_translate("widget", "<html><head/><body><p>点击选择输入文件夹路径</p></body></html>"))
        self.pushButton_input.setText(_translate("widget", "输入"))
        self.lineEdit_input.setPlaceholderText(_translate("widget", "选择输入路径"))
        self.lineEdit_output.setPlaceholderText(_translate("widget", "选择输出路径"))
        self.label_title.setText(_translate("widget", "采 集 工 具 集"))
        self.pushButton_output.setToolTip(_translate("widget", "<html><head/><body><p>点击选择输出文件夹路径</p></body></html>"))
        self.pushButton_output.setText(_translate("widget", "输出"))
        self.pushButton_help.setToolTip(_translate("widget", "<html><head/><body><p>点击打开帮助文档</p></body></html>"))
        self.pushButton_help.setText(_translate("widget", "帮  助"))
        self.pushButton_sure.setText(_translate("widget", "确  定"))
        self.pushButton_num7.setText(_translate("widget", "7"))
        self.pushButton_num8.setText(_translate("widget", "8"))
        self.pushButton_num9.setText(_translate("widget", "9"))
        self.pushButton_num4.setText(_translate("widget", "4"))
        self.pushButton_num5.setText(_translate("widget", "5"))
        self.pushButton_num6.setText(_translate("widget", "6"))
        self.pushButton_num1.setText(_translate("widget", "1"))
        self.pushButton_num2.setText(_translate("widget", "2"))
        self.pushButton_num3.setText(_translate("widget", "3"))
        self.pushButton_chear.setText(_translate("widget", "C"))
        self.pushButton_num0.setText(_translate("widget", "0"))
        self.pushButton_yes.setText(_translate("widget", "Y"))
        self.label_nums.setText(_translate("widget", "拨 号 界 面"))
        self.lcdNumber_thread_nums.setToolTip(_translate("widget", "<html><head/><body><p>当前运行线程数</p></body></html>"))
        self.label_logs.setText(_translate("widget", "日 志 界 面"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_widget()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
