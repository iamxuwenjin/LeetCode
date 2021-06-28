#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time : 2021/4/2 5:56 下午
Author : wenjin.xu
Site : 
File : 41.缺失的第一个正整数.py
Software: PyCharm
description：
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
"""


# class Solution(object):
#     @staticmethod
#     def first_missing_positive(nums: list):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return
#         pre_num = 0
#         while nums:
#             num = nums[0]
#             for i in range(len(nums)):
#                 if nums[i] < num:
#                     num = nums[i]
#             nums.remove(num)
#             if pre_num == num:
#                 continue
#             else:
#                 if num < 0:
#                     continue
#                 if num - pre_num > 1:
#                     return pre_num + 1
#             pre_num = num
#
#         return pre_num + 1
#
#
# if __name__ == '__main__':
#     num_list = [3, 4, -1, 1]
#     s = Solution()
#     res = s.first_missing_positive(num_list)
#     print(res)

class Solution(object):
    @staticmethod
    def first_missing_positive(nums: list):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        length = len(nums)
        for i in range(length):
            if nums[i] < 0:
                nums[i] = length + 1
        for i in range(length):
            num = abs(nums[i])
            if num < length:
                nums[num - 1] = -abs(nums[num - 1])
        for i in range(length):
            if nums[i] > 0:
                return i + 1

        return length + 1

        pass


if __name__ == '__main__':
    num_list = [7, 8, 9, 11, 12]
    s = Solution()
    res = s.first_missing_positive(num_list)
    print(res)
