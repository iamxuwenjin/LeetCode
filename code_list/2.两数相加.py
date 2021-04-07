#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time : 2020/8/21 6:02 下午
Author : wenjin.xu
Site :
File : 两数之和.py
Software: PyCharm
description：
给出两个非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0开头。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    @staticmethod
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        val_1 = l1.val
        val_2 = l2.val
        flag = (val_1 + val_2) // 10
        res_val = (val_1 + val_2) % 10
        res_list = [str(res_val)]
        l1_next = l1.next
        l2_next = l2.next
        while (l1_next is not None) or (l2_next is not None) or flag:
            val_1 = 0 if l1_next is None else l1_next.val
            val_2 = 0 if l2_next is None else l2_next.val
            sum_num = val_1 + val_2 + flag
            flag = sum_num // 10
            res_val = sum_num % 10
            res_list.insert(0, str(res_val))
            l1_next = l1_next.next if l1_next is not None else None
            l2_next = l2_next.next if l2_next is not None else None
        num = ''.join(res_list)
        len_num = len(num)
        result = ListNode(int(num[0]))
        for i in range(1, len_num):
            result = ListNode(int(num[i]), result)
        return result


