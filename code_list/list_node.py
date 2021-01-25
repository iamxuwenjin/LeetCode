# -*- coding: utf-8 -*-
"""
@Time    : 2020/12/14 22:58
@Author  : wenjin.xu
@File    : list_node.py
@Comment: "链表相关测试工具"
"""


class ListNode(object):
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def get_list_node(data: list) -> ListNode:
    list_node = None
    while data:
        val = data.pop()
        list_node = ListNode(val, list_node)
    return list_node


class SingleLinkList(object):
    def __init__(self):
        self.head = None


    def add(self, key):
        pass

    def find(self, key):
        pass

    def move_to_front(self):
        pass

    def __len__(self):
        count = 0
        node = self.head
        while node.next:
            count += 1
            node = node.next
        return count
