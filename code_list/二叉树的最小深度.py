#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time : 2020/8/21 3:59 下午
Author : wenjin.xu
Site : 
File : 二叉树的最小深度.py
Software: PyCharm
description：
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        l, r = self.minDepth(root.left), self.minDepth(root.right)
        if root.left and root.right:
            return 1 + min(l, r)
        else:
            return 1 + l + r


