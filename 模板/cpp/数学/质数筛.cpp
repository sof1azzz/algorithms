//
// Created by 123 on 25-7-23.
//
#include "bits/stdc++.h"
using namespace std;
using ll = long long;

// 埃拉托色尼筛法（Sieve of Eratosthenes）
const int N = 1e6 + 10;
vector<bool> is_prime(N, true); // is_prime[i] 表示 i 是否是质数
vector<int> primes; // 存质数列表

void eratosthenes(int n) {
	is_prime[0] = is_prime[1] = false;
	for (int i = 2; i <= n; ++i) {
		if (is_prime[i]) {
			primes.push_back(i);
			for (int j = i * 2; j <= n; j += i)
				is_prime[j] = false;
		}
	}
}

// 线性筛（欧拉筛法）：更快，O(n)
void linear_sieve(int n) {
	is_prime[0] = is_prime[1] = false;
	for (int i = 2; i <= n; ++i) {
		if (is_prime[i]) primes.push_back(i);
		for (int p: primes) {
			if (p * i > n) break;
			is_prime[p * i] = false;
			// 还可以加一个prime_factor[p * i] = p,最小质因数
			if (i % p == 0) break; // 保证每个数只被最小质因子筛掉
		}
	}
}
