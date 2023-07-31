# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: mutli_process.py
@time: 2023/7/31 17:48
@desc:

"""

from cup.util import ThreadPool
from settings.setting import MAXTHREADS


class MulitProcess(ThreadPool):
    """

    """

    def __init__(self):
        super(MulitProcess, self).__init__()

    def make_start(self):
        self.pool = ThreadPool(
            minthreads=3,
            maxthreads=MAXTHREADS,
            daemon_threads=True)
        return self.pool

    def get_thread_len(self):
        dic = self.pool.get_stats()
        return dic["queue_len"] - dic["thread_num"]
