#差分を利用するいもす法
#従来の値からどれだけたしひきするのかを記録するリストdiffを作成
#時間で変化する設定で使えそう

N, W = map(int, input().split())

MAXT = 200000
diff = [0] * (MAXT+2)

for _ in range(N):
  s, t, p = map(int, input().split())
  diff[s] += p
  diff[t] -= p
  
cur = 0
for x in diff:
  cur += x
  if cur > W:
    print("No")
    break
else:
  print("Yes")
