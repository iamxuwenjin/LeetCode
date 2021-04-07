#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time : 2021/4/6 5:37 下午
Author : wenjin.xu
Site : 
File : 442.数组中的重复数据.py
Software: PyCharm
description：
"""


class Solution:
    @staticmethod
    def find_duplicates(nums: list) -> list:
        if not nums:
            return []
        res = []
        n = len(nums)
        for i in range(n):
            num = abs(nums[i])
            if nums[num - 1] < 0:
                res.append(num)
            nums[num - 1] = -nums[num - 1]
        return res


if __name__ == '__main__':
    data = [4, 3, 2, 7, 8, 2, 3, 1]
    s = Solution()
    print(s.find_duplicates(data))
