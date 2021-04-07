#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time : 2021/4/7 3:51 下午
Author : wenjin.xu
Site : 
File : 3.无重复字符的最长子串.py
Software: PyCharm
description：给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
"""


class Solution:
    @staticmethod
    def length_of_longest_sub_string(s: str) -> int:
        # 遍历O(n^2)
        n = len(s)
        count = 1
        if n == 1:
            return count
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if s[i] == s[j]:
        #             if j - i > count:
        #                 count = j - i
        #             break

        # 滑动窗口
        # 开始枚举每一个字符
        j = 1
        dup = set()
        i = 0
        while i < n:
            val = s[i]
            # 找到与字符串第一个字符相同的字符
            while j < n:
                r_val = s[j]
                if val == r_val:
                    if j - i > count:
                        count = j - i
                    break
                j += 1
        return count


if __name__ == '__main__':
    string = 'pwwkew'
    ins = Solution()
    print(ins.length_of_longest_sub_string(string))
