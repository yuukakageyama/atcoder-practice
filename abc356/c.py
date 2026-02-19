#bit全探索
#各鍵の選び方で矛盾がないかを全部調べる

N,M, K = map(int, input().split())

tests = []

#テストケースをM行分読み込む
for _ in range(M):
  parts = input().split()
  C = int(parts[0])
  A = list(map(int, parts[1:1+C])) #1~Cまで
  r = parts[1+C] #'○' or '×'
  
  #テストで挿した鍵の集合をビット列で表す
  tmask = 0
  for a in A:
    #|=はorして代入
    tmask |= 1 << (a-1) #右からa番目が1になるものを代入していく
  
  tests.append((tmask, r)) #tmaskはbit列，rは〇×
  
ans = 0

#各鍵の選び方に関して
for mask in range(1<<N):
  ok = True
  
  #テストケース1個ずつチェック
  for tmask, r in tests:
    #今回調べているmask & 各テストケースtmaskで挿した鍵の中で本物だったものだけ
    real = (mask &tmask).bit_count()
    
    #テスト結果が〇のとき : 本物がK本以上ないと矛盾
    if r == 'o':
      if real < K:
        ok = False
        break #矛盾が見つかったら次のmaskへ
    #テスト結果が×のとき : 本物がK本以上あると矛盾
    else:
      if real >= K:
        ok = False
        break #矛盾が見つかったら次のmaskへ
  if ok:
      ans += 1 #調べていたmaskは正解
print(ans)
