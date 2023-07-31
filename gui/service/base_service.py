# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: base_service.py
@time: 2023/7/31 19:37
@desc:

"""
from utils.mutli_process import MulitProcess
from utils.utils_signal import Single


class BaseService(Single):
    def __init__(self):
        super(BaseService, self).__init__()
        self.mp = MulitProcess()
        self.pool = self.mp.make_start()
        self.pool.start()

    def task(self, **kwargs):
        """

        :param kwargs:
        :return:
        """

    def callback(self, status, result):
        """

        :param status:
        :param result:
        :return:
        """
        self.emit_int(self.mp.get_thread_len())
        if status:
            self.emit_str(str(result))
        else:
            self.emit_str("<font color=red>{}</font>".format(str(result)))

    def process(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        in_path = kwargs["in_path"]
        out_path = kwargs["out_path"]
        for i in range(1, 100):
            self.pool.add_1job_with_callback(self.callback,
                                             self.task,
                                             in_path=in_path,
                                             out_path=out_path
                                             )

        self.pool.stop()
