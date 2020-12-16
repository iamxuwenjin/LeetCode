# -*- coding: utf-8 -*-
"""
@Time    : 2020/12/16 16:55
@Author  : wenjin.xu
@File    : 不同路径.py
@Comment: "LeetCode NO.62"
"""

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？
"""

import numpy as np


# f(m, n) = f(m-1, n) + f(m, n-1)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 递归解决，性能极差
        """
        if m <= 1 or n <= 1:
            return 1
        else:
            return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        """
        data_list = [[0]*n for _ in range(m)]

        for i in range(m):
            data_list[i][0] = 1
        for j in range(n):
            data_list[0][j] = 1
        # array = np.array(data_list)

        for j in range(1, n):
            for i in range(1, m):
                data_list[i][j] = data_list[i - 1][j] + data_list[i][j - 1]
        return data_list[-1][-1]


if __name__ == '__main__':
    s = Solution()
    res = s.uniquePaths(3, 4)
    print(res)
