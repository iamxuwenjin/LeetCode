# -*- coding: utf-8 -*-
"""
@Time    : 2020/12/16 17:40
@Author  : wenjin.xu
@File    : 最小路径和.py
@Comment: "Leetcode No.64"
"""
import numpy as np

"""给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。"""


class Solution:
    def minPathSum(self, grid) -> int:
        array = np.array(grid)
        m = len(grid)
        n = len(grid[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    res[0][0] = grid[0][0]
                    continue
                elif j == 0:
                    res[i][0] = res[i - 1][0] + grid[i][0]
                    continue
                elif i == 0:
                    res[0][j] = res[0][j - 1] + grid[0][j]
                    continue
                res[i][j] = min(res[i - 1][j], res[i][j - 1]) + grid[i][j]
        # res[i][j] = min(res[i-1, j], res[i, j-1]) + grid[m-1][n-1]
        temp = np.array(res)
        return res[m - 1][n - 1]


if __name__ == '__main__':
    # data = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    data = [[1, 2, 3], [4, 5, 6]]

    # data = [[1, 3]]
    s = Solution()
    s.minPathSum(data)
