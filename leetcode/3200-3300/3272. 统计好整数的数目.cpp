#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
#include <functional>
#include <algorithm>
#include <ranges>
#include <numeric>
#include <unordered_set>
#include <cmath>   
#include <memory> 
#include <map>

using namespace std;

class Solution {
public:
    long long countGoodIntegers(int n, int k) {
        vector<int> factorial(n + 1);
        factorial[0] = 1;
        for (int i = 1; i <= n; i++) {
            factorial[i] = factorial[i - 1] * i;
        }

        long long ans = 0;
        unordered_set<string> vis;
        int base = pow(10, (n - 1) / 2);
        for (int i = base; i < base * 10; i++) { // 枚举回文数左半边
            string s = to_string(i);
            s += string(s.rbegin() + (n % 2), s.rend());
            if (stoll(s) % k) { // 回文数不能被 k 整除
                continue;
            }

            ranges::sort(s);
            
            if (!vis.insert(s).second) { // 不能重复统计
                continue;
            }

            int cnt[10]{};
            for (char c : s) {
                cnt[c - '0']++;
            }
            int res = (n - cnt[0]) * factorial[n - 1];
            for (int c : cnt) {
                res /= factorial[c];
            }
            ans += res;
        }
        return ans;
    }
};