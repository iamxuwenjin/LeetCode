#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time : 2021/4/12 8:12 下午
Author : wenjin.xu
Site : 
File : 215. 数组中的第K个最大元素.py
Software: PyCharm
description：在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
"""


class Solution:
    def find_Kth_largest(self, nums: list, k: int) -> int:
        n = len(nums)
        if k == n:
            # 当K等于n时，第K大的数为数组中最小的数
            v = nums[0]
            for i in range(1, n):
                if nums[i] < v:
                    v = nums[i]
            return v
        # 利用堆排序查找，排序的过程就是查找的过程
        # 最后一个父节点
        for i in range(n // 2 - 1, -1, -1):
            self.heap_sort(nums, i, n - 1)

        last_idx = n - 1
        while last_idx > 0:
            nums[0], nums[last_idx] = nums[last_idx], nums[0]
            if n - last_idx == k:
                return nums[-k]
            self.heap_sort(nums, 0, last_idx - 1)
            last_idx -= 1

    def heap_sort(self, nums: list, root_idx, length):
        """
        构建大顶堆
        :param nums:
        :param root_idx:
        :param length:
        :return:
        """
        idx = root_idx * 2 + 1

        while idx <= length:
            if idx < length and nums[idx] < nums[idx + 1]:
                idx += 1
            if nums[root_idx] < nums[idx]:
                nums[root_idx], nums[idx] = nums[idx], nums[root_idx]
                root_idx = idx
                idx = idx * 2 + 1
            else:
                break


if __name__ == '__main__':
    a = [3, 2, 1, 5, 6, 4]
    so = Solution()
    print(so.find_Kth_largest(a, 2))
