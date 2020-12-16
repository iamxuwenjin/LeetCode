# -*- coding: utf-8 -*-
"""
@Time    : 2020/12/14 22:59
@Author  : wenjin.xu
@File    : dynamic_programming.py
@Comment: "动态规划学习"
"""


"""
问题描述：一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
f(n) = f(n-1) + f(n-2)
"""


def demo(n):
    if n <= 1:
        return 1
    return demo(n-1) + demo(n-2)


if __name__ == '__main__':
    res = demo(6)
    print(res)

