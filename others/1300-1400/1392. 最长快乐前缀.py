from collections import *
from functools import *
from math import *
from itertools import *
from heapq import *
from bisect import *
from typing import *
from queue import *

MOD = int(1e9 + 7)
DIRS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        nxt = [0] * n
        length = 0
        for i in range(1, n):
            while length > 0 and s[i] != s[length]:
                length = nxt[length - 1]
            if s[i] == s[length]:
                length += 1
            nxt[i] = length
        return s[: nxt[-1]]


class Solution:
    def get_z(self, s: str) -> List[int]:
        n = len(s)
        z = [0] * n
        l, r = 0, 0
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                l, r = i, i + z[i] - 1
                z[i] += 1
        return z

    def longestPrefix(self, s: str) -> str:
        z = self.get_z(s)
        ans = 0
        n = len(s)
        for i, x in enumerate(z):
            if n - x == i and x > ans:
                ans = x

        return s[:ans]


class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        z = [0] * n
        l, r = 0, 0
        ans = 0
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                l, r = i, i + z[i] - 1
                z[i] += 1
            if n - i == z[i] and z[i] > ans:
                ans = z[i]
        return s[:ans]
