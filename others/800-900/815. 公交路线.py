from collections import *
from functools import *
from math import *
from itertools import *
from heapq import *
from bisect import *
from typing import *
from queue import *
from string import *

MOD = int(1e9 + 7)
DIRS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        graph = defaultdict(list)
        for i, route in enumerate(routes):
            for x in route:
                graph[x].append(i)

        vis = set()
        dq = deque()
        dq.append((source, 0))
        vis.add(source)
        while dq:
            x, d = dq.popleft()
            if x == target:
                return d
            for bus in graph[x]:
                if routes[bus]:
                    for stop in routes[bus]:
                        if stop not in vis:
                            dq.append((stop, d + 1))
                routes[bus].clear()
        return -1


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        # 记录经过车站 x 的公交车编号
        stop_to_buses = defaultdict(list)
        for i, route in enumerate(routes):
            for x in route:
                stop_to_buses[x].append(i)

        # 小优化：如果没有公交车经过起点或终点，直接返回
        if source not in stop_to_buses or target not in stop_to_buses:
            # 注意原地 TP 的情况
            return -1 if source != target else 0

        # BFS
        dis = {source: 0}
        q = deque([source])
        while q:
            x = q.popleft()  # 当前在车站 x
            dis_x = dis[x]
            for i in stop_to_buses[x]:  # 遍历所有经过车站 x 的公交车 i
                if routes[i]:
                    for y in routes[i]:  # 遍历公交车 i 的路线
                        if y not in dis:  # 没有访问过车站 y
                            dis[y] = dis_x + 1  # 从 x 站上车然后在 y 站下车
                            q.append(y)
                    routes[i] = None  # 标记 routes[i] 遍历过

        return dis.get(target, -1)
