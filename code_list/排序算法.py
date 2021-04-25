#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time : 2021/4/21 4:20 下午
Author : wenjin.xu
Site : 
File : 排序算法.py
Software: PyCharm
description：排序算法整理
"""


class NumberSort(object):

    def quick_sort(self, array: list):
        """
         分解： 将数组 a[l⋯r] 「划分」成两个子数组 a[l⋯q−1]、a[q+1⋯r]，
         使得 a[l⋯q−1] 中的每个元素小于等于 a[q]a[q]，且 a[q]a[q] 小于等于 a[q+1⋯r] 中的每个元素。
         其中，计算下标 q 也是「划分」过程的一部分。
         解决： 通过递归调用快速排序，对子数组 a[l⋯q−1] 和 a[q+1⋯r] 进行排序。
         合并： 因为子数组都是原址排序的，所以不需要进行合并操作，a[l⋯r] 已经有序。
         """
        if len(array) < 2:
            return array
        else:
            pivot = array[0]
            less = [i for i in array[1:] if i <= pivot]
            greater = [i for i in array[1:] if i > pivot]
            return self.quick_sort(less) + [pivot] + self.quick_sort(greater)

    def heap_sort(self, array: list):
        """
        父节点索引：(i-1)/2
        左孩子索引：2*i+1
        右孩子索引：2*i+2

        :param array:
        :return: sorted list
        堆排序  heap_sort
                      0,4
                   /       \\
                 1,7         2,0
               /     \\       /    \\
             3,9       4,1  5,5     6,3
           /    \\      /
         7,3     8,2  9,6

        nums = [4, 7, 0, 9, 1, 5, 3, 3, 2, 6]
        根据列表长度，找到最后一个非叶子节点，开始循化到 root 根节点，制作 大顶堆
        """
        length = len(array)
        last_idx = length - 1  # 最后一个元素的 索引
        last_p_node_idx = length // 2 - 1

        # 构建一个大顶堆
        for i in range(last_p_node_idx, -1, -1):
            self.heap_adjust(array, i, last_idx)

        while last_idx > 0:
            # swap(lst, 0, last)
            array[0], array[last_idx] = array[last_idx], array[0]
            # 调整堆让 adjust 处理，最后已经排好序的数，就不处理了
            self.heap_adjust(array, 0, last_idx - 1)
            last_idx -= 1

        return array  # 将列表返回

    @staticmethod
    def heap_adjust(array, root_idx, last_idx):
        """
        调整root节点与子节点的顺序
        :param last_idx: 最大索引
        :param array: 待调整列表
        :param root_idx: root 节点索引
        :return: 大顶堆列表
        """
        # 需要继续向下查找的root idx
        idx = root_idx * 2 + 1
        while idx <= last_idx:
            if idx < last_idx and array[idx] < array[idx + 1]:  # 如果这儿不判断 j < high 可能超出索引
                # 比较两个子节点，取大者的idx
                idx = idx + 1
            if array[root_idx] < array[idx]:  # 与最大的子节点比较，如果小于子节点则交换位置
                array[root_idx], array[idx] = array[idx], array[root_idx]
                root_idx = idx
                idx = idx * 2 + 1  # 记录交过换过位置的子节点的子节点索引
            else:
                break



if __name__ == '__main__':
    ns = NumberSort()
    res = ns.heap_sort([4, 7, 0, 9, 1, 5, 3, 3, 2, 6])
    print(res)
