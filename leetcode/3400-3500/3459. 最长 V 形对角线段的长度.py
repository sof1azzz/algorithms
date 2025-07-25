from typing import List
from functools import *
from math import *

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        DIRS = (1, 1), (1, -1), (-1, -1), (-1, 1)
        m, n = len(grid), len(grid[0])

        # 上一步在 (i,j)，移动方向为 DIRS[k]，是否可以右转，当前位置目标值
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（一行代码实现记忆化）
        def dfs(i: int, j: int, k: int, can_turn: bool, target: int) -> int:
            i += DIRS[k][0]
            j += DIRS[k][1]
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != target:
                return 0
            res = dfs(i, j, k, can_turn, 2 - target)  # 直行
            if can_turn:
                res = max(res, dfs(i, j, (k + 1) % 4, False, 2 - target))  # 右转
            return res + 1  # 算上当前位置

        ans = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    # 枚举起始方向
                    for k in range(4):
                        ans = max(ans, dfs(i, j, k, True, 2) + 1)
        return ans
