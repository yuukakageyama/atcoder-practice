#貪欲法(安い店から買う)
#あとどれだけ必要か，をneedで更新
#価格*本数で合計本数とか見やすく
#append忘れ注意

N, M = map(int, input().split())

shops = []
for _ in range(N):
  a, b = map(int, input().split())
  shops.append((a,b))

shops.sort()

ans = 0
need = M

for a, b in shops:
  if need == 0:
    break
  
  #この店で買う本数, b本置いてあるからといって全部買うとわけではないので注意
  buy = min(b, need)
  ans += a*buy #価格*本数= 合計金額
  need -= buy #必要な本数を更新
  
print(ans)
