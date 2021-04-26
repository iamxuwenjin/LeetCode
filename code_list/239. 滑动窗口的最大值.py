#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time : 2021/4/21 7:08 下午
Author : wenjin.xu
Site : 
File : 239. 滑动窗口的最大值.py
Software: PyCharm
description：给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。
"""
import heapq


class Solution:
    def max_sliding_window(self, nums: list, k: int) -> list:
        n = len(nums)
        # 构建大根堆
        window = [(i, nums[i]) for i in range(k)]
        for i in range(k // 2 - 1, -1, -1):
            self._heapify(window, i, k - 1)
        ans = [window[0][1]]
        start = 1
        while start + k - 1 < n:
            window.append((start + k - 1, nums[start + k - 1]))

            for i in range(len(window) // 2 - 1, -1, -1):
                self._heapify(window, i, len(window) - 1)

            # 判断堆顶的元素是否在窗口内
            while window[0][0] < start:
                window = window[1:]
                for i in range(len(window) // 2 - 1, -1, -1):
                    self._heapify(window, i, len(window) - 1)
            ans.append(window[0][1])
            start += 1
        return ans

    def _heapify(self, nums, root_idx, last_idx):
        idx = root_idx * 2 + 1
        while idx <= last_idx:
            if idx < last_idx and nums[idx][1] < nums[idx + 1][1]:
                idx += 1
            if nums[root_idx][1] < nums[idx][1]:
                nums[root_idx], nums[idx] = nums[idx], nums[root_idx]
                root_idx = idx
                idx = idx * 2 + 1
            else:
                break


if __name__ == '__main__':
    s = Solution()
    nums = [4, -2]
    k = 2
    res = s.max_sliding_window(nums, k)
    print(res)
