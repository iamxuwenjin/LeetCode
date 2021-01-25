#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time : 2021/1/25 2:18 下午
Author : wenjin.xu
Site : 
File : lru.py
Software: PyCharm
description：
"""


class LRU(object):
    def __init__(self):
        self.cap = 4
        self.node_list = []
        self.data_dict = {}

    def get(self, key):
        if key in self.data_dict:
            self.node_list.remove(key)
            self.node_list.insert(0, key)
            return self.data_dict[key]
        else:
            return

    def set(self, key, value):
        # 如果存在，则更新，且将key放在队头
        if key in self.data_dict:
            self.data_dict.pop(key)
            self.data_dict[key] = value
            self.node_list.remove(key)
            self.node_list.insert(0, key)
        # 如果为新增，判断队列长度
        elif len(self.data_dict) == self.cap:
            old_key = self.node_list.pop()
            self.data_dict.pop(old_key)
            self.node_list.insert(0, key)
            self.data_dict[key] = value
        else:
            self.data_dict[key] = value
            self.node_list.insert(0, key)
