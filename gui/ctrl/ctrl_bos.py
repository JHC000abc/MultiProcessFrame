# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: ctrl_bos.py
@time: 2023/7/31 21:25
@desc: 

"""
from gui.ctrl.input_output_main_ctrl import IOMainWindow
from gui.service.service_bos import ServiceBos


class BosMainWindow(IOMainWindow):
    def __init__(self,root_path):
        super(BosMainWindow, self).__init__(root_path)
        self._init_slot()

        self.nums_msg_map["9418"] = {
            "desc": "启航",
            "func": ServiceBos().process
        }

    def _init_slot(self):
        ServiceBos().single_int.connect(self.show_threads_nums)
        ServiceBos().single_str.connect(self.show_single_log)
        ServiceBos().single_dict.connect(self.show_single_dict)

