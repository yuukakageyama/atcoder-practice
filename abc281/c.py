#二分探索のライブラリbisectを利用
#累積和も利用
#既に配列があってその中の位置を探すときはbisect
#配列じゃなくて答えを探す問題のとき　手書きで二分探索


import bisect
N, T = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)
T %= total

#累積和　各曲の終わり時刻
pref = []
s = 0
for a in A:
  s += a
  pref.append(s)

# Tは曲の途中なので T < pref[i]となる最初のiを探す
#bisect_rightで配列prefで値Tを二分探索して右側の挿入点を探す
#bisect_rightはTより大きい最初の位置
#bisect_leftはT以上の最初の位置
i = bisect.bisect_right(pref, T)

#曲番号は
song = i + 1

#曲の開始時刻
start = 0 if i == 0 else pref[i-1]

#曲が始まってから何秒か
sec = T - start

print(song, sec)
