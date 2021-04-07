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
        # n = len(s)
        # count = 1
        # if n == 1:
        #     return count
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if s[i] == s[j]:
        #             if j - i > count:
        #                 count = j - i
        #             break

        # 滑动窗口
        # 开始枚举每一个字符
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans


if __name__ == '__main__':
    string = "abcabcbb"
    ins = Solution()
    print(ins.length_of_longest_sub_string(string))
