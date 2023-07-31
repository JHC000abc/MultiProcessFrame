# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: service_bos.py
@time: 2023/7/31 16:43
@desc:

"""
import time
from gui.service.base_service import BaseService


def single(func):
    """
    单例
    :param func:
    :return:
    """
    instance = {}

    def wrapper(*args, **kwargs):
        if func not in instance:
            instance[func] = func(*args, **kwargs)
        return instance[func]
    return wrapper


@single
class ServiceBos(BaseService):
    """

    """

    def task(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        time.sleep(1)
        return {"status": 0, "msg": ""}


if __name__ == '__main__':
    sb = ServiceBos()
    sb.process()
