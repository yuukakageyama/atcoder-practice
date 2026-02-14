import sys
input = sys.stdin.readline

N, K, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

# 累積和
pref = [0] * (N + 1)
for i in range(N):
    pref[i + 1] = pref[i] + A[i]

def range_sum(l, r):
    return pref[r] - pref[l]
#ここまでは前と一緒

# m が条件を満たすかどうか
def ok(m):
    #飲まない方N-m個にお酒を配置したときにも飲む日本酒の個数
    r = max(0, K - (N - m))
    if r == 0:
        return False
    #大きい方から飲むことを考える
    start = N - m #飲む集合A[n-m:N]
    #Aの中にr個日本酒があるときそれが小さい方から配置されてしまう
    worst = range_sum(start, start + r)
    return worst >= X

# 二分探索
left = 1
right = N
ans = -1

while left <= right:
    mid = (left + right) // 2
    if ok(mid):
        ans = mid
        right = mid - 1   # もっと小さい m を探す
    else:
        left = mid + 1

print(ans)
