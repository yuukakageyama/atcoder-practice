
N,M = map(int, input().split())

S= []

for i in range(N):
  si = input().strip()
  mask = 0
  for j, c in enumerate(si): #enumerateで位置と文字を同時にとれる
    if c == 'o':
      mask |= 1 << j
  S.append(mask)

all_flavors = (1 << M) - 1 #111...っていう整数
ans = 10**9

#各mask(0,1のならび)でまわる売り場を全パターン探索
for mask in range(1<<N): #売り場はN個
  now = 0
  cnt = 0
  for i in range(N):
    if(mask >> i) & 1: #i番目だけ取り出して1だったら
      now |= S[i] #orして代入
      cnt += 1 #回る売り場の個数cnt
  
  #全部の味がそろっていたら最小を更新
  if now == all_flavors:
    if cnt < ans:
      ans = cnt
print(ans)
