cmake_minimum_required(VERSION 3.31)
project(leetcode)

set(CMAKE_CXX_STANDARD 23)

add_executable(leetcode
        others/0-100/1.cpp
        "others/0-100/19. 删除链表的倒数第 N 个结点.cpp"
        "others/0-100/2. 两数相加.cpp"
        "others/0-100/21. 合并两个有序链表.cpp"
        "others/0-100/23. 合并 K 个升序链表.cpp"
        "others/0-100/25. K 个一组翻转链表.cpp"
        "others/0-100/3. 无重复字符的最长子串.cpp"
        "others/0-100/30. 串联所有单词的子串.cpp"
        "others/0-100/34. 在排序数组中查找元素的第一个和最后一个位置.cpp"
        "others/0-100/35. 搜索插入位置.cpp"
        "others/0-100/4. 寻找两个正序数组的中位数.cpp"
        "others/0-100/41. 缺失的第一个正数.cpp"
        "others/0-100/50. Pow(x, n).cpp"
        "others/0-100/53. 最大子数组和.cpp"
        "others/0-100/61. 旋转链表.cpp"
        "others/0-100/62. 不同路径.cpp"
        "others/0-100/63. 不同路径 II.cpp"
        "others/0-100/64. 最小路径和.cpp"
        "others/0-100/72. 编辑距离.cpp"
        "others/0-100/75. 颜色分类.cpp"
        "others/0-100/76. 最小覆盖子串.cpp"
        "others/0-100/82. 删除排序链表中的重复元素 II.cpp"
        "others/0-100/83. 删除排序链表中的重复元素.cpp"
        "others/0-100/86. 分隔链表.cpp"
        others/0-100/92反转链表2.cpp
        "others/0-100/94. 二叉树的中序遍历.cpp"
        "others/0-100/97. 交错字符串.cpp"
        "others/100-200/120. 三角形最小路径和.cpp"
        "others/100-200/121. 买卖股票的最佳时机.cpp"
        "others/100-200/138. 随机链表的复制.cpp"
        "others/100-200/141. 环形链表.cpp"
        "others/100-200/142. 环形链表 II.cpp"
        "others/100-200/143. 重排链表.cpp"
        "others/100-200/144. 二叉树的前序遍历.cpp"
        "others/100-200/145. 二叉树的后序遍历.cpp"
        "others/100-200/146. LRU 缓存.cpp"
        "others/100-200/147. 对链表进行插入排序.cpp"
        "others/100-200/148. 排序链表.cpp"
        "others/100-200/152. 乘积最大子数组.cpp"
        "others/100-200/160. 相交链表.cpp"
        "others/100-200/174. 地下城游戏.cpp"
        "others/100-200/198. 打家劫舍.cpp"
        "others/1000-1100/1004. 最大连续1的个数 III.cpp"
        "others/1000-1100/1007. 行相等的最少多米诺旋转.cpp"
        "others/1000-1100/1011. 在 D 天内送达包裹的能力.cpp"
        "others/1000-1100/1016. 子串能表示从 1 到 N 数字的二进制串.cpp"
        "others/1000-1100/1019. 链表中的下一个更大节点.cpp"
        "others/1000-1100/1049. 最后一块石头的重量 II.cpp"
        "others/1000-1100/1052. 爱生气的书店老板.cpp"
        "others/1000-1100/1092. 最短公共超序列.cpp"
        "others/1100-1200/1128. 等价多米诺骨牌对的数量.cpp"
        "others/1100-1200/1143. 最长公共子序列.cpp"
        "others/1100-1200/1146. 快照数组.cpp"
        "others/1100-1200/1155. 掷骰子等于目标和的方法数.cpp"
        "others/1100-1200/1170. 比较字符串最小字母出现频次.cpp"
        "others/1100-1200/1171. 从链表中删去总和值为零的连续节点.cpp"
        "others/1100-1200/1191. K 次串联后最大子数组之和.cpp"
        "others/1200-1300/1206. 设计跳表.cpp"
        "others/1200-1300/1208. 尽可能使字符串相等.cpp"
        "others/1200-1300/1283. 使结果不超过阈值的最小除数.cpp"
        "others/1200-1300/1289. 下降路径最小和 II.cpp"
        "others/1200-1300/1290. 二进制链表转整数.cpp"
        "others/1200-1300/1295. 统计位数为偶数的数字.cpp"
        "others/1200-1300/1297. 子串的最大出现次数.cpp"
        "others/1300-1400/1301. 最大得分的路径数目.cpp"
        "others/1300-1400/1343. 大小为 K 且平均值大于等于阈值的子数组数目.cpp"
        "others/1300-1400/1385. 两个数组间的距离值.cpp"
        "others/1300-1400/1399. 统计最大组的数目.cpp"
        "others/1400-1500/1423. 可获得的最大点数.cpp"
        "others/1400-1500/1449. 数位成本和为目标值的最大数字.cpp"
        "others/1400-1500/1456. 定长子串中元音的最大数目.cpp"
        "others/1400-1500/1458. 两个子序列的最大点积.cpp"
        "others/1400-1500/1461. 检查一个字符串是否包含所有长度为 K 的二进制子串.cpp"
        "others/1400-1500/1463. 摘樱桃 II.cpp"
        "others/1400-1500/1482. 制作 m 束花所需的最少天数.cpp"
        "others/1400-1500/1483. 树节点的第 K 个祖先.cpp"
        "others/1400-1500/1493. 删掉一个元素以后全为 1 的最长子数组.cpp"
        "others/1500-1600/1534. 统计好三元组.cpp"
        "others/1500-1600/1550. 存在连续三个奇数的数组.cpp"
        "others/1500-1600/1594. 矩阵的最大非负积.cpp"
        "others/1600-1700/1626. 无矛盾的最佳球队.cpp"
        "others/1600-1700/1652. 拆炸弹.cpp"
        "others/1600-1700/1658. 将 x 减到 0 的最小操作数.cpp"
        "others/1600-1700/1669. 合并两个链表.cpp"
        "others/1600-1700/1671. 得到山形数组的最少删除次数.cpp"
        "others/1600-1700/1695. 删除子数组的最大得分.cpp"
        "others/1700-1800/1721. 交换链表中的节点.cpp"
        "others/1700-1800/1749. 任意子数组和的绝对值的最大值.cpp"
        "others/1700-1800/1774. 最接近目标价格的甜点成本.cpp"
        "others/1800-1900/1802. 有界数组中指定下标处的最大值.cpp"
        "others/1800-1900/1818. 绝对差值和.cpp"
        "others/1800-1900/1824. 最少侧跳次数.cpp"
        "others/1800-1900/1870. 准时到达的列车最小时速.cpp"
        "others/1800-1900/1888. 使二进制字符串字符交替的最少反转次数.cpp"
        "others/1800-1900/1898. 可移除字符的最大数目.cpp"
        "others/1900-2000/1920. 基于排列构建数组.cpp"
        "others/1900-2000/1922. 统计好数字的数目.cpp"
        "others/1900-2000/1931. 用三种不同颜色为网格涂色.cpp"
        "others/1900-2000/1937. 扣分后的最大得分.cpp"
        "others/1900-2000/1964. 找出到每个位置为止最长的有效障碍赛跑路线.cpp"
        "others/1900-2000/1981. 最小化目标值与所选元素的差.cpp"
        "others/1900-2000/1984. 学生分数的最小差值.cpp"
        "others/200-300/203. 移除链表元素.cpp"
        "others/200-300/204. 计数质数.cpp"
        "others/200-300/213. 打家劫舍 II.cpp"
        "others/200-300/215. 数组中的第K个最大元素.cpp"
        "others/200-300/220. 存在重复元素 III.cpp"
        others/200-300/221最大正方形.cpp
        "others/200-300/235. 二叉搜索树的最近公共祖先.cpp"
        "others/200-300/236. 二叉树的最近公共祖先.cpp"
        "others/200-300/237. 删除链表中的节点.cpp"
        "others/200-300/264. 丑数 II.cpp"
        "others/200-300/275. H 指数 II.cpp"
        "others/200-300/279. 完全平方数.cpp"
        "others/200-300/282. 给表达式添加运算符.cpp"
        "others/200-300/287. 寻找重复数.cpp"
        "others/2000-2100/2024. 考试的最大困扰度.cpp"
        "others/2000-2100/2058. 找出临界点之间的最小和最大距离.cpp"
        "others/2000-2100/2070. 每一个查询的最大美丽值.cpp"
        "others/2000-2100/2071. 你可以安排的最多任务数目.cpp"
        "others/2000-2100/2074. 反转偶数长度组的节点.cpp"
        "others/2000-2100/2080. 区间内查询数字的频率.cpp"
        "others/2000-2100/2090. 半径为 k 的子数组平均值.cpp"
        "others/2000-2100/2094. 找出 3 位偶数.cpp"
        "others/2000-2100/2095. 删除链表的中间节点.cpp"
        "others/2100-2200/2134. 最少交换次数来组合所有的 1 II.cpp"
        "others/2100-2200/2140. 解决智力问题.cpp"
        "others/2100-2200/2145. 统计隐藏数组数目.cpp"
        "others/2100-2200/2156. 查找给定哈希值的子串.cpp"
        "others/2100-2200/2176. 统计数组中相等且可以被整除的数对.cpp"
        "others/2100-2200/2179. 统计数组中好三元组数目.cpp"
        "others/2100-2200/2181. 合并零之间的节点.cpp"
        "others/2100-2200/2187. 完成旅途的最少时间.cpp"
        "others/2200-2300/2218. 从栈中取出 K 个硬币的最大面值和.cpp"
        "others/2200-2300/2224. 转化时间需要的最少操作数.cpp"
        "others/2200-2300/2226. 每个小孩最多能分到多少糖果.cpp"
        "others/2200-2300/2266. 统计打字方案数.cpp"
        "others/2200-2300/2267. 检查是否有合法括号字符串路径.cpp"
        "others/2200-2300/2269. 找到一个数字的 K 美丽值.cpp"
        "others/2300-2400/2300. 咒语和药水的成功对数.cpp"
        "others/2300-2400/2302. 统计得分小于 K 的子数组数目.cpp"
        "others/2300-2400/2304. 网格中的最小路径代价.cpp"
        "others/2300-2400/2320. 统计放置房子的方式数.cpp"
        "others/2300-2400/2321. 拼接数组的最大分数.cpp"
        "others/2300-2400/2328. 网格图中递增路径的数目.cpp"
        "others/2300-2400/2364. 统计坏数对的数目.cpp"
        "others/2300-2400/2379. 得到 K 个黑块的最少涂色次数.cpp"
        "others/2300-2400/2389. 和有限的最长子序列.cpp"
        "others/2400-2500/2435. 矩阵中和能被 K 整除的路径.cpp"
        "others/2400-2500/2444. 统计定界子数组的数目.cpp"
        "others/2400-2500/2461. 长度为 K 子数组中的最大和.cpp"
        "others/2400-2500/2466. 统计构造好字符串的方案数.cpp"
        "others/2400-2500/2487. 从链表中移除节点.cpp"
        "others/2500-2600/2518. 好分区的数目.cpp"
        "others/2500-2600/2529. 正整数和负整数的最大计数.cpp"
        "others/2500-2600/2537. 统计好子数组的数目.cpp"
        others/2500-2600/2563.公平数.cpp
        "others/2500-2600/2576. 求出最多标记下标.cpp"
        "others/2500-2600/2585. 获得分数的方法数.cpp"
        "others/2500-2600/2594. 修车的最少时间.cpp"
        "others/2600-2700/2606. 找到最大开销的子字符串.cpp"
        "others/2600-2700/2653. 滑动子数组的美丽值.cpp"
        "others/2600-2700/2684. 矩阵中移动的最大次数.cpp"
        "others/2700-2800/2742. 给墙壁刷油漆.cpp"
        "others/2700-2800/2787. 将一个数字表示成幂的和的方案数.cpp"
        "others/2700-2800/2799. 统计完全子数组的数目.cpp"
        "others/2800-2900/2807. 在链表中插入最大公约数.cpp"
        "others/2800-2900/2816. 翻倍以链表形式表示的数字.cpp"
        "others/2800-2900/2841. 几乎唯一子数组的最大和.cpp"
        "others/2800-2900/2845. 统计趣味子数组的数目.cpp"
        "others/2900-3000/2900. 最长相邻不相等子序列 I.cpp"
        "others/2900-3000/2901. 最长相邻不相等子序列 II.cpp"
        "others/2900-3000/2902. 和带限制的子多重集合的数目.cpp"
        "others/2900-3000/2915. 和为目标值的最长子序列的长度.cpp"
        "others/2900-3000/2918. 数组的最小相等和.cpp"
        "others/2900-3000/2953. 统计完全子字符串.cpp"
        "others/2900-3000/2958. 最多 K 个重复元素的最长子数组.cpp"
        "others/2900-3000/2962. 统计最大元素出现至少 K 次的子数组.cpp"
        "others/2900-3000/2981. 找出出现至少三次的最长特殊子字符串 I.cpp"
        "others/2900-3000/2982. 找出出现至少三次的最长特殊子字符串 II.cpp"
        "others/300-400/322. 零钱兑换.cpp"
        "others/300-400/328. 奇偶链表.cpp"
        "others/300-400/329. 矩阵中的最长递增路径.cpp"
        "others/300-400/377. 组合总和 Ⅳ.cpp"
        "others/300-400/382. 链表随机节点.cpp"
        "others/300-400/389. 找不同.cpp"
        "others/300-400/398. 随机数索引.cpp"
        "others/3000-3100/3048. 标记所有下标的最早秒数 I.cpp"
        "others/3000-3100/3082. 求出所有子序列的能量和.cpp"
        "others/3000-3100/3090. 每个字符最多出现两次的最长子字符串.cpp"
        "others/3100-3200/3180. 执行操作可获得的最大总奖励 I.cpp"
        "others/3100-3200/3181. 执行操作可获得的最大总奖励 II.cpp"
        "others/3200-3300/3217. 从链表中移除在数组中存在的节点.cpp"
        "others/3200-3300/3272. 统计好整数的数目.cpp"
        "others/3200-3300/3287. 求出数组中最大序列值.cpp"
        "others/3200-3300/3296. 移山所需的最少秒数.cpp"
        "others/3300-3400/3330. 找到初始输入字符串 I.cpp"
        "others/3300-3400/3333. 找到初始输入字符串 II.cpp"
        "others/3300-3400/3335. 字符串转换后的长度 I.cpp"
        "others/3300-3400/3337. 字符串转换后的长度 II.cpp"
        "others/3300-3400/3341. 到达最后一个房间的最少时间 I.cpp"
        "others/3300-3400/3342. 到达最后一个房间的最少时间 II.cpp"
        "others/3300-3400/3363. 最多可收集的水果数目.cpp"
        "others/3300-3400/3392. 统计符合条件长度为 3 的子数组数目.cpp"
        "others/3300-3400/3393. 统计异或值为给定值的路径数目.cpp"
        "others/3400-3500/3418. 机器人可以获得的最大金币数.cpp"
        "others/3400-3500/3439. 重新安排会议得到最多空余时间 I.cpp"
        "others/3400-3500/3453. 分割正方形 I.cpp"
        "others/3400-3500/3459. 最长 V 形对角线段的长度.cpp"
        "others/3400-3500/3488. 距离最小相等元素查询.cpp"
        "others/3400-3500/3489. 零数组变换 IV.cpp"
        "others/3400-3500/3492. 船上可以装载的最大集装箱数量.cpp"
        "others/3400-3500/3493. 属性图.cpp"
        "others/3400-3500/3494. 酿造药水需要的最少总时间.cpp"
        "others/3400-3500/3495. 使数组元素都变为零的最少操作次数.cpp"
        "others/3500-3600/3508. 设计路由器.cpp"
        "others/3500-3600/3545. 不同字符数量最多为 K 时的最少删除数.cpp"
        "others/3500-3600/3546. 等和矩阵分割 I.cpp"
        others/3500-3600/3547.cpp
        "others/3500-3600/3550. 数位和等于下标的最小下标.cpp"
        "others/3500-3600/3551. 数位和排序需要的最小交换次数.cpp"
        "others/3500-3600/3552. 网格传送门旅游.cpp"
        "others/3500-3600/3553. 包含给定路径的最小带权子树 II.cpp"
        "others/400-500/403. 青蛙过河.cpp"
        "others/400-500/416. 分割等和子集.cpp"
        "others/400-500/421. 数组中两个数的最大异或值.cpp"
        "others/400-500/430. 扁平化多级双向链表.cpp"
        "others/400-500/432. 全 O(1) 的数据结构.cpp"
        "others/400-500/438. 找到字符串中所有字母异位词.cpp"
        "others/400-500/445. 两数相加 II.cpp"
        "others/400-500/457. 环形数组是否存在循环.cpp"
        "others/400-500/458. 可怜的小猪(信息熵).cpp"
        "others/400-500/460. LFU 缓存.cpp"
        "others/400-500/474. 一和零.cpp"
        "others/400-500/475. 供暖器.cpp"
        "others/400-500/494. 目标和.cpp"
        "others/500-600/501. 二叉搜索树中的众数.cpp"
        "others/500-600/518. 零钱兑换 II.cpp"
        "others/500-600/567. 字符串的排列.cpp"
        "others/500-600/583. 两个字符串的删除操作.cpp"
        "others/600-700/643. 子数组最大平均数 I.cpp"
        "others/600-700/658. 找到 K 个最接近的元素.cpp"
        "others/600-700/673. 最长递增子序列的个数.cpp"
        "others/600-700/790. 多米诺和托米诺平铺.cpp"
        "others/700-800/704. 二分查找.cpp"
        "others/700-800/707. 设计链表.cpp"
        "others/700-800/712. 两个字符串的最小ASCII删除和.cpp"
        "others/700-800/725. 分隔链表.cpp"
        "others/700-800/740. 删除并获得点数.cpp"
        "others/700-800/741. 摘樱桃.cpp"
        "others/700-800/744. 寻找比目标字母大的最小字母.cpp"
        "others/700-800/746. 使用最小花费爬楼梯.cpp"
        "others/700-800/781. 森林中的兔子.cpp"
        "others/800-900/805. 数组的均值分割.cpp"
        "others/800-900/817. 链表组件.cpp"
        "others/800-900/838. 推多米诺.cpp"
        "others/800-900/875. 爱吃香蕉的珂珂875爱吃鸡巴的傻逼.cpp"
        "others/800-900/876. 链表的中间结点.cpp"
        "others/800-900/879. 盈利计划.cpp"
        "others/900-1000/904. 水果成篮.cpp"
        "others/900-1000/911. 在线选举.cpp"
        "others/900-1000/918. 环形子数组的最大和.cpp"
        "others/900-1000/956. 最高的广告牌.cpp"
        "others/LCP/LCP 08. 剧情触发时间.cpp"
        "others/LCP/LCP 47. 入场安检.cpp"
        "others/LCR/LCR 029. 循环有序列表的插入.cpp"
        others/分类/二分查找/1-LAPTOP-PGRI81JH.cpp
        others/分类/二分查找/1.cpp
        "others/分类/二分查找/1146. 快照数组.cpp"
        "others/分类/二分查找/1170. 比较字符串最小字母出现频次.cpp"
        "others/分类/二分查找/1385. 两个数组间的距离值.cpp"
        others/分类/二分查找/153寻找旋转排序数组的最小值.cpp
        "others/分类/二分查找/154. 寻找旋转排序数组中的最小值 II.cpp"
        others/分类/二分查找/162寻找峰值.cpp
        "others/分类/二分查找/1818. 绝对差值和.cpp"
        others/分类/二分查找/1901寻找峰值2.cpp
        "others/分类/二分查找/2070. 每一个查询的最大美丽值.cpp"
        "others/分类/二分查找/2080. 区间内查询数字的频率.cpp"
        others/分类/二分查找/2187完成旅途的最少时间.cpp
        "others/分类/二分查找/2300. 咒语和药水的成功对数.cpp"
        "others/分类/二分查找/2389. 和有限的最长子序列.cpp"
        others/分类/二分查找/2439最小化数组中的最大数.cpp
        others/分类/二分查找/2517礼盒的最大甜蜜度.cpp
        "others/分类/二分查找/2529. 正整数和负整数的最大计数.cpp"
        others/分类/二分查找/2563.公平数.cpp
        others/分类/二分查找/275.H指数.cpp
        others/分类/二分查找/2861最大合金数.cpp
        others/分类/二分查找/33寻找旋转排序数组的目标值.cpp
        "others/分类/二分查找/34. 在排序数组中查找元素的第一个和最后一个位置.cpp"
        "others/分类/二分查找/3488. 距离最小相等元素查询.cpp"
        "others/分类/二分查找/35. 搜索插入位置.cpp"
        "others/分类/二分查找/658. 找到 K 个最接近的元素.cpp"
        "others/分类/二分查找/704. 二分查找.cpp"
        "others/分类/二分查找/744. 寻找比目标字母大的最小字母.cpp"
        "others/分类/二分查找/875. 爱吃香蕉的珂珂875爱吃鸡巴的傻逼.cpp"
        others/分类/二分查找/875爱吃香蕉的傻逼.cpp
        "others/分类/二分查找/981. 基于时间的键值存储.cpp"
        others/分类/二叉树/1.cpp
        others/分类/二叉树/100.相同的树.cpp
        others/分类/二叉树/101.对称二叉树.cpp
        "others/分类/二叉树/102. 二叉树的层序遍历.cpp"
        "others/分类/二叉树/1026. 节点与其祖先之间的最大差值.cpp"
        "others/分类/二叉树/103. 二叉树的锯齿形层序遍历.cpp"
        "others/分类/二叉树/104. 二叉树的最大深度.cpp"
        "others/分类/二叉树/105. 从前序与中序遍历序列构造二叉树.cpp"
        "others/分类/二叉树/106. 从中序与后序遍历序列构造二叉树.cpp"
        "others/分类/二叉树/107. 二叉树的层序遍历 II.cpp"
        "others/分类/二叉树/1080. 根到叶路径上的不足节点.cpp"
        "others/分类/二叉树/110. 平衡二叉树.cpp"
        "others/分类/二叉树/111. 二叉树的最小深度.cpp"
        "others/分类/二叉树/1110. 删点成林.cpp"
        "others/分类/二叉树/112. 路径总和.cpp"
        "others/分类/二叉树/1123. 最深叶节点的最近公共祖先.cpp"
        "others/分类/二叉树/113. 路径总和 II.cpp"
        "others/分类/二叉树/116. 填充每个节点的下一个右侧节点指针.cpp"
        "others/分类/二叉树/117. 填充每个节点的下一个右侧节点指针 II.cpp"
        others/分类/二叉树/129.求根节点到叶节点数字之和.cpp
        "others/分类/二叉树/1302. 层数最深叶子节点的和.cpp"
        "others/分类/二叉树/1372. 二叉树中的最长交错路径.cpp"
        others/分类/二叉树/1448.统计二叉树中好节点的个数.cpp
        "others/分类/二叉树/1609. 奇偶树.cpp"
        "others/分类/二叉树/199. 二叉树的右视图.cpp"
        "others/分类/二叉树/2096. 从二叉树一个节点到另一个节点每一步的方向.cpp"
        "others/分类/二叉树/226. 翻转二叉树.cpp"
        "others/分类/二叉树/230. 二叉搜索树中第 K 小的元素.cpp"
        "others/分类/二叉树/2331. 计算布尔二叉树的值.cpp"
        "others/分类/二叉树/235. 二叉搜索树的最近公共祖先.cpp"
        "others/分类/二叉树/236. 二叉树的最近公共祖先.cpp"
        "others/分类/二叉树/2415. 反转二叉树的奇数层.cpp"
        "others/分类/二叉树/2476. 二叉搜索树最近节点查询.cpp"
        "others/分类/二叉树/257. 二叉树的所有路径.cpp"
        "others/分类/二叉树/2583. 二叉树中的第 K 大层和.cpp"
        "others/分类/二叉树/2641. 二叉树的堂兄弟节点 II.cpp"
        "others/分类/二叉树/501. 二叉搜索树中的众数.cpp"
        "others/分类/二叉树/508. 出现次数最多的子树元素和.cpp"
        "others/分类/二叉树/513. 找树左下角的值.cpp"
        "others/分类/二叉树/530. 二叉搜索树的最小绝对差.cpp"
        "others/分类/二叉树/617. 合并二叉树.cpp"
        others/分类/二叉树/700.二叉搜索树中的搜索.cpp
        "others/分类/二叉树/783. 二叉搜索树节点最小距离.cpp"
        "others/分类/二叉树/865. 具有所有最深节点的最小子树.cpp"
        "others/分类/二叉树/938. 二叉搜索树的范围和.cpp"
        "others/分类/二叉树/951. 翻转等价二叉树.cpp"
        "others/分类/二叉树/965. 单值二叉树.cpp"
        "others/分类/二叉树/987. 二叉树的垂序遍历.cpp"
        "others/分类/动态规划/数位dp/1399. 统计最大组的数目.cpp"
        "others/分类/动态规划/数位dp/2843. 统计对称整数的数目.cpp"
        "others/分类/动态规划/数位dp/2999. 统计强大整数的数目.cpp"
        "others/分类/动态规划/数位dp/600. 不含连续1的非负整数.cpp"
        "others/分类/动态规划/树状/2179. 统计数组中好三元组数目.cpp"
        "others/分类/动态规划/线性dp/1092. 最短公共超序列.cpp"
        "others/分类/动态规划/线性dp/1143. 最长公共子序列.cpp"
        "others/分类/动态规划/线性dp/1458. 两个子序列的最大点积.cpp"
        "others/分类/动态规划/线性dp/1626. 无矛盾的最佳球队.cpp"
        "others/分类/动态规划/线性dp/1671. 得到山形数组的最少删除次数.cpp"
        "others/分类/动态规划/线性dp/1964. 找出到每个位置为止最长的有效障碍赛跑路线.cpp"
        "others/分类/动态规划/线性dp/2320. 统计放置房子的方式数.cpp"
        "others/分类/动态规划/线性dp/300. 最长递增子序列.cpp"
        "others/分类/动态规划/线性dp/354. 俄罗斯套娃信封问题.cpp"
        "others/分类/动态规划/线性dp/583. 两个字符串的删除操作.cpp"
        "others/分类/动态规划/线性dp/673. 最长递增子序列的个数.cpp"
        "others/分类/动态规划/线性dp/712. 两个字符串的最小ASCII删除和.cpp"
        "others/分类/动态规划/线性dp/72. 编辑距离.cpp"
        "others/分类/动态规划/线性dp/97. 交错字符串.cpp"
        "others/分类/动态规划/网格/120. 三角形最小路径和.cpp"
        "others/分类/动态规划/网格/1289. 下降路径最小和 II.cpp"
        "others/分类/动态规划/网格/1301. 最大得分的路径数目.cpp"
        "others/分类/动态规划/网格/1463. 摘樱桃 II.cpp"
        "others/分类/动态规划/网格/1594. 矩阵的最大非负积.cpp"
        "others/分类/动态规划/网格/174. 地下城游戏.cpp"
        "others/分类/动态规划/网格/1824. 最少侧跳次数.cpp"
        "others/分类/动态规划/网格/1937. 扣分后的最大得分.cpp"
        others/分类/动态规划/网格/221最大正方形.cpp
        "others/分类/动态规划/网格/2267. 检查是否有合法括号字符串路径.cpp"
        "others/分类/动态规划/网格/2304. 网格中的最小路径代价.cpp"
        "others/分类/动态规划/网格/2328. 网格图中递增路径的数目.cpp"
        "others/分类/动态规划/网格/2435. 矩阵中和能被 K 整除的路径.cpp"
        "others/分类/动态规划/网格/2684. 矩阵中移动的最大次数.cpp"
        "others/分类/动态规划/网格/329. 矩阵中的最长递增路径.cpp"
        "others/分类/动态规划/网格/3363. 最多可收集的水果数目.cpp"
        "others/分类/动态规划/网格/3393. 统计异或值为给定值的路径数目.cpp"
        "others/分类/动态规划/网格/3418. 机器人可以获得的最大金币数.cpp"
        "others/分类/动态规划/网格/3459. 最长 V 形对角线段的长度.cpp"
        "others/分类/动态规划/网格/403. 青蛙过河.cpp"
        "others/分类/动态规划/网格/62. 不同路径.cpp"
        "others/分类/动态规划/网格/63. 不同路径 II.cpp"
        "others/分类/动态规划/网格/64. 最小路径和.cpp"
        "others/分类/动态规划/网格/741. 摘樱桃.cpp"
        "others/分类/动态规划/网格/931. 下降路径最小和.cpp"
        "others/分类/动态规划/背包/2787. 将一个数字表示成幂的和的方案数.cpp"
        "others/分类/动态规划/背包/279. 完全平方数.cpp"
        "others/分类/动态规划/背包/2915. 和为目标值的最长子序列的长度.cpp"
        "others/分类/动态规划/背包/322. 零钱兑换.cpp"
        "others/分类/动态规划/背包/416. 分割等和子集.cpp"
        "others/分类/动态规划/背包/494. 目标和.cpp"
        "others/分类/动态规划/背包/518. 零钱兑换 II.cpp"
        "others/分类/动态规划/121. 买卖股票的最佳时机.cpp"
        "others/分类/动态规划/1373. 二叉搜索子树的最大键值和.cpp"
        "others/分类/动态规划/198. 打家劫舍.cpp"
        "others/分类/动态规划/213. 打家劫舍 II.cpp"
        "others/分类/动态规划/2140. 解决智力问题.cpp"
        "others/分类/动态规划/2266. 统计打字方案数.cpp"
        "others/分类/动态规划/2466. 统计构造好字符串的方案数.cpp"
        "others/分类/动态规划/2606. 找到最大开销的子字符串.cpp"
        "others/分类/动态规划/3186. 施咒的最大总伤害.cpp"
        "others/分类/动态规划/368. 最大整除子集.cpp"
        "others/分类/动态规划/377. 组合总和 Ⅳ.cpp"
        "others/分类/动态规划/70. 爬楼梯.cpp"
        "others/分类/动态规划/740. 删除并获得点数.cpp"
        "others/分类/动态规划/746. 使用最小花费爬楼梯.cpp"
        "others/分类/动态规划/805. 数组的均值分割.cpp"
        "others/分类/动态规划/98. 验证二叉搜索树.cpp"
        others/分类/双指针/11盛最多水的容器.cpp
        others/分类/双指针/15三数之和.cpp
        others/分类/双指针/167两数之和.cpp
        others/分类/双指针/16最接近的三数之和.cpp
        others/分类/双指针/18四数之和.cpp
        others/分类/双指针/2824统计和小于目标的下标对数目.cpp
        others/分类/双指针/42接雨水.cpp
        others/分类/双指针/611有效三角形的个数.cpp
        "others/分类/双指针/LCR 139. 训练计划 I.cpp"
        "others/分类/回溯/1239. 串联字符串的最大长度.cpp"
        "others/分类/回溯/131. 分割回文串-LAPTOP-PGRI81JH.cpp"
        "others/分类/回溯/131. 分割回文串.cpp"
        "others/分类/回溯/17. 电话号码的字母组合.cpp"
        "others/分类/回溯/1863. 找出所有子集的异或总和再求和.cpp"
        "others/分类/回溯/216. 组合总和 III.cpp"
        "others/分类/回溯/22. 括号生成.cpp"
        "others/分类/回溯/2212. 射箭比赛中的最大得分.cpp"
        "others/分类/回溯/2397. 被列覆盖的最多行数.cpp"
        "others/分类/回溯/2477. 到达首都的最少油耗.cpp"
        "others/分类/回溯/2698. 求一个整数的惩罚数.cpp"
        "others/分类/回溯/2850. 将石头分散到网格图的最少移动次数.cpp"
        "others/分类/回溯/301. 删除无效的括号.cpp"
        "others/分类/回溯/306. 累加数.cpp"
        "others/分类/回溯/357. 统计各位数字都不同的数字个数.cpp"
        "others/分类/回溯/39. 组合总和.cpp"
        "others/分类/回溯/46. 全排列.cpp"
        "others/分类/回溯/47. 全排列 II.cpp"
        "others/分类/回溯/51. N 皇后.cpp"
        "others/分类/回溯/52. N 皇后II.cpp"
        "others/分类/回溯/77. 组合.cpp"
        "others/分类/回溯/78. 子集.cpp"
        "others/分类/回溯/784. 字母大小写全排列.cpp"
        "others/分类/回溯/93. 复原 IP 地址.cpp"
        "others/分类/回溯/LCP 51. 烹饪料理.cpp"
        "others/分类/数组/前缀和/1732. 找到最高海拔.cpp"
        "others/分类/数组/2126. 摧毁小行星.cpp"
        "others/分类/数组/2411. 按位或最大的最小子数组长度.cpp"
        "others/分类/数组/26. 删除有序数组中的重复项.cpp"
        "others/分类/数组/31. 下一个排列.cpp"
        "others/分类/数组/3120. 统计特殊字母的数量 I.cpp"
        "others/分类/数组/3137. K 周期字符串需要的最少操作次数.cpp"
        "others/分类/数组/3375. 使数组的值全部为 K 的最少操作次数.cpp"
        "others/分类/数组/3396. 使数组元素互不相同所需的最少操作次数.cpp"
        "others/分类/数组/416. 分割等和子集.cpp"
        "others/分类/数组/68. 文本左右对齐.cpp"
        "others/分类/数组/944. 删列造序.cpp"
        "others/分类/数组/985. 查询后的偶数和.cpp"
        "others/分类/数组/LCR 135. 报数.cpp"
        "others/分类/数组/LCR 158. 库存管理 II.cpp"
        "others/分类/数组/LCR 182. 动态口令.cpp"
        others/分类/树/1.cpp
        others/分类/树/100.相同的树.cpp
        others/分类/树/101.对称二叉树.cpp
        "others/分类/树/102. 二叉树的层序遍历.cpp"
        "others/分类/树/1026. 节点与其祖先之间的最大差值.cpp"
        "others/分类/树/103. 二叉树的锯齿形层序遍历.cpp"
        "others/分类/树/104. 二叉树的最大深度.cpp"
        "others/分类/树/105. 从前序与中序遍历序列构造二叉树.cpp"
        "others/分类/树/106. 从中序与后序遍历序列构造二叉树.cpp"
        "others/分类/树/107. 二叉树的层序遍历 II.cpp"
        "others/分类/树/1080. 根到叶路径上的不足节点.cpp"
        "others/分类/树/110. 平衡二叉树.cpp"
        "others/分类/树/111. 二叉树的最小深度.cpp"
        "others/分类/树/1110. 删点成林.cpp"
        "others/分类/树/112. 路径总和.cpp"
        "others/分类/树/1123. 最深叶节点的最近公共祖先.cpp"
        "others/分类/树/113. 路径总和 II.cpp"
        "others/分类/树/116. 填充每个节点的下一个右侧节点指针.cpp"
        "others/分类/树/117. 填充每个节点的下一个右侧节点指针 II.cpp"
        others/分类/树/129.求根节点到叶节点数字之和.cpp
        "others/分类/树/1302. 层数最深叶子节点的和.cpp"
        "others/分类/树/1372. 二叉树中的最长交错路径.cpp"
        others/分类/树/1448.统计二叉树中好节点的个数.cpp
        "others/分类/树/1609. 奇偶树.cpp"
        "others/分类/树/199. 二叉树的右视图.cpp"
        "others/分类/树/208. 实现 Trie (前缀树).cpp"
        "others/分类/树/2096. 从二叉树一个节点到另一个节点每一步的方向.cpp"
        "others/分类/树/226. 翻转二叉树.cpp"
        "others/分类/树/230. 二叉搜索树中第 K 小的元素.cpp"
        "others/分类/树/2331. 计算布尔二叉树的值.cpp"
        "others/分类/树/235. 二叉搜索树的最近公共祖先.cpp"
        "others/分类/树/236. 二叉树的最近公共祖先.cpp"
        "others/分类/树/2415. 反转二叉树的奇数层.cpp"
        "others/分类/树/2476. 二叉搜索树最近节点查询.cpp"
        "others/分类/树/257. 二叉树的所有路径.cpp"
        "others/分类/树/2583. 二叉树中的第 K 大层和.cpp"
        "others/分类/树/2641. 二叉树的堂兄弟节点 II.cpp"
        "others/分类/树/501. 二叉搜索树中的众数.cpp"
        "others/分类/树/508. 出现次数最多的子树元素和.cpp"
        "others/分类/树/513. 找树左下角的值.cpp"
        "others/分类/树/530. 二叉搜索树的最小绝对差.cpp"
        "others/分类/树/617. 合并二叉树.cpp"
        others/分类/树/700.二叉搜索树中的搜索.cpp
        "others/分类/树/783. 二叉搜索树节点最小距离.cpp"
        "others/分类/树/865. 具有所有最深节点的最小子树.cpp"
        "others/分类/树/938. 二叉搜索树的范围和.cpp"
        "others/分类/树/951. 翻转等价二叉树.cpp"
        "others/分类/树/965. 单值二叉树.cpp"
        "others/分类/树/987. 二叉树的垂序遍历.cpp"
        "others/分类/模拟类/数组/3178. 找出 K 秒后拿着球的孩子.cpp"
        "others/分类/模拟类/网格/1138. 字母板上的路径.cpp"
        others/分类/滑动窗口/1.cpp
        "others/分类/滑动窗口/1004最大连续1的个数 III.cpp"
        "others/分类/滑动窗口/1052. 爱生气的书店老板.cpp"
        "others/分类/滑动窗口/1297. 子串的最大出现次数.cpp"
        "others/分类/滑动窗口/1343. 大小为 K 且平均值大于等于阈值的子数组数目.cpp"
        "others/分类/滑动窗口/1423. 可获得的最大点数.cpp"
        "others/分类/滑动窗口/1456. 定长子串中元音的最大数目.cpp"
        "others/分类/滑动窗口/1652. 拆炸弹.cpp"
        "others/分类/滑动窗口/1658. 将 x 减到 0 的最小操作数.cpp"
        "others/分类/滑动窗口/2090. 半径为 k 的子数组平均值.cpp"
        others/分类/滑动窗口/209长度最小的子数组.cpp
        "others/分类/滑动窗口/2134. 最少交换次数来组合所有的 1 II.cpp"
        "others/分类/滑动窗口/2302统计得分小于 K 的子数组数目.cpp"
        "others/分类/滑动窗口/2379. 得到 K 个黑块的最少涂色次数.cpp"
        "others/分类/滑动窗口/2461. 长度为 K 子数组中的最大和.cpp"
        "others/分类/滑动窗口/2537. 统计好子数组的数目.cpp"
        "others/分类/滑动窗口/2653. 滑动子数组的美丽值.cpp"
        others/分类/滑动窗口/2730找到最长的半重复子字符串.cpp
        "others/分类/滑动窗口/2799. 统计完全子数组的数目.cpp"
        "others/分类/滑动窗口/2841. 几乎唯一子数组的最大和.cpp"
        "others/分类/滑动窗口/2958最多 K 个重复元素的最长子数组.cpp"
        "others/分类/滑动窗口/2962统计最大元素出现至少 K 次的子数组.cpp"
        "others/分类/滑动窗口/3439. 重新安排会议得到最多空余时间 I.cpp"
        others/分类/滑动窗口/3无重复字符的最长子串.cpp
        "others/分类/滑动窗口/643. 子数组最大平均数 I.cpp"
        "others/分类/滑动窗口/713乘积小于 K 的子数组.cpp"
        "others/分类/滑动窗口/76. 最小覆盖子串.cpp"
        "others/分类/链表/前后指针/19. 删除链表的倒数第 N 个结点.cpp"
        "others/分类/链表/前后指针/203. 移除链表元素.cpp"
        "others/分类/链表/前后指针/237. 删除链表中的节点.cpp"
        "others/分类/链表/前后指针/82. 删除排序链表中的重复元素 II.cpp"
        "others/分类/链表/前后指针/83. 删除排序链表中的重复元素.cpp"
        others/分类/链表/反转链表/1.cpp
        "others/分类/链表/反转链表/206. 反转链表.cpp"
        "others/分类/链表/反转链表/24. 两两交换链表中的节点.cpp"
        "others/分类/链表/反转链表/25. K 个一组翻转链表.cpp"
        others/分类/链表/反转链表/2816翻倍链表元素.cpp
        others/分类/链表/反转链表/445.两数相加2.cpp
        others/分类/链表/反转链表/92反转链表2.cpp
        "others/分类/链表/快慢指针/141. 环形链表.cpp"
        others/分类/链表/快慢指针/142.环形链表2.cpp
        "others/分类/链表/快慢指针/2130. 链表最大孪生和.cpp"
        others/分类/链表/快慢指针/234.回文链表.cpp
        "others/分类/链表/快慢指针/876. 链表的中间结点.cpp"
        "others/分类/链表/1290. 二进制链表转整数.cpp"
        "others/分类/链表/146. LRU 缓存.cpp"
        "others/分类/链表/147. 对链表进行插入排序.cpp"
        "others/分类/链表/2058. 找出临界点之间的最小和最大距离.cpp"
        "others/分类/链表/2074. 反转偶数长度组的节点.cpp"
        "others/分类/链表/21. 合并两个有序链表.cpp"
        "others/分类/链表/2181. 合并零之间的节点.cpp"
        "others/分类/链表/2487. 从链表中移除节点.cpp"
        "others/分类/链表/3217. 从链表中移除在数组中存在的节点.cpp"
        "others/分类/链表/61. 旋转链表.cpp"
        "others/分类/链表/725. 分隔链表.cpp"
        "others/分类/链表/817. 链表组件.cpp"
        "others/分类/链表/LCR 029. 循环有序列表的插入.cpp"
        1.cpp
        "模板.cpp"
        "others/3000-3100/3024. 三角形类型.cpp"
        "others/2700-2800/2730. 找到最长的半重复子字符串.cpp"
        "others/3300-3400/3355. 零数组变换 I.cpp"
        "others/2300-2400/2342. 数位和相等数对的最大和.cpp"
        "others/2800-2900/2861. 最大合金数.cpp"
        "others/2700-2800/2779. 数组的最大美丽值.cpp"
        "others/400-500/404. 左叶子之和.cpp"
        "others/600-700/671. 二叉树中第二小的节点.cpp"
        "others/2200-2300/3007. 价值和小于等于 K 的最大数字.cpp"
        "others/1800-1900/1838. 最高频元素的频数.cpp"
        "others/3300-3400/3362. 零数组变换 III.cpp"
        "others/2100-2200/2141. 同时运行 N 台电脑的最长时间.cpp"
        "others/2500-2600/2516. 每种字符至少取 K 个.cpp"
        "others/3000-3100/3068. 最大节点价值之和.cpp"
        "others/3000-3100/3007. 价值和小于等于 K 的最大数字.cpp"
        "others/2200-2300/2258. 逃离火灾.cpp"
        "others/2800-2900/2831. 找出最长等值子数组.cpp"
        "others/600-700/624. 数组列表中的最大距离.cpp"
        "others/1000-1100/1010. 总持续时间可被 60 整除的歌曲.cpp"
        "others/100-200/129. 求根节点到叶节点数字之和.cpp"
        "others/2000-2100/2001. 可互换矩形的组数.cpp"
        "others/2200-2300/2271. 毯子覆盖的最多白色砖块数.cpp"
        "others/2100-2200/2131. 连接两字母单词得到的最长回文串.cpp"
        "others/LCP/LCP 78. 城墙防线.cpp"
        "others/3300-3400/3316. 从原字符串里进行删除操作的最多次数3316. 从原字符串里进行删除操作的最多次数.cpp"
        "others/200-300/233. 数字 1 的个数.cpp"
        "others/100-200/199. 二叉树的右视图.cpp"
        "others/1400-1500/1448. 统计二叉树中好节点的数目.cpp"
        "others/1400-1500/1457. 二叉树中的伪回文路径.cpp"
        "others/2700-2800/2791. 树中可以形成回文的路径数.cpp"
        "others/1800-1900/1857. 有向图中最大颜色值.cpp"
        "others/200-300/207. 课程表.cpp"
        "others/2500-2600/2506. 统计相似字符串对的数目.cpp"
        "others/1600-1700/1639. 通过给定词典构造目标字符串的方案数.cpp"
        "others/1300-1400/1315. 祖父节点值为偶数的节点和.cpp"
        "others/500-600/547. 省份数量.cpp"
        "others/2800-2900/2894. 分类求和并作差.cpp"
        "others/1900-2000/1971. 寻找图中是否存在路径.cpp"
        "others/1600-1700/1648. 销售价值减少的颜色球.cpp"
        "others/2100-2200/2106. 摘水果.cpp"
        "others/100-200/111. 二叉树的最小深度.cpp"
        "others/2800-2900/2874. 有序三元组中的最大值 II.cpp"
        "others/1300-1400/1392. 最长快乐前缀.cpp")
