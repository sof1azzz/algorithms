//
// Created by 123 on 25-5-19.
//

#include <algorithm>
#include <array>
#include <bitset>
#include <cmath>
#include <cstring>
#include <functional>
#include <iostream>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <random>
#include <ranges>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;
class Solution {
public:
  int numIdenticalPairs(vector<int>& nums) {
    std::pmr::unordered_map<int, int> map;
    int ans = 0;
    for (int x : nums) {
      ans += map[x];
      map[x]++;
    }
    return ans;
  }
};
