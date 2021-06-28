#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time : 2021/4/8 10:46 上午
Author : wenjin.xu
Site : 
File : 4. 寻找两个正序数组的中位数.py
Software: PyCharm
description：给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
"""


class Solution:
    def find_median_sorted_arrays(self, nums1: list, nums2: list) -> float:
        """
        :param nums1:
        :param nums2:
        :return:
        """
        # O(m+n),两个有序集合合并相当于归并排序的一个步骤，
        m = len(nums1)
        n = len(nums2)
        median = (m + n) // 2
        i, j = 0, 0
        ans = []
        if not nums1:
            ans = nums2
        elif not nums2:
            ans = nums1
        else:
            while True:
                if i >= m:
                    ans.extend(nums2[j:])
                    break
                if j >= n:
                    ans.extend(nums1[i:])
                    break
                if nums1[i] < nums2[j]:
                    ans.append(nums1[i])
                    i += 1
                else:
                    ans.append(nums2[j])
                    j += 1
        print(ans)
        if (m + n) % 2 == 0:
            return (ans[median] + ans[median - 1]) / 2
        else:
            return ans[median]


if __name__ == '__main__':
    data_1 = [1, 3, 5, 6, 7]
    data_2 = [2, 3]
    so = Solution()
    print(so.find_median_sorted_arrays(data_1, data_2))
