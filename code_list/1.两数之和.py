#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time : 2020/8/21 6:02 下午
Author : wenjin.xu
Site : 
File : 两数之和.py
Software: PyCharm
description：
给定一个整数数组 nums和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
"""


class Solution:
    def twoSum(self, nums: list, target: int) -> [int]:
        for i, v in enumerate(nums):
            nums[i] = None
            if target - v in nums:
                return [i, nums.index(target - v)]


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum(nums=[2, 11, 7, 15], target=9))
