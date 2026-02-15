#bit演算演習，こっちの方が簡単かも

N, K = map(int, input().split())

S = []
for _ in range(N):
  S.append(input().strip())

ans = 0

#各文字の選び方に対して
for mask in range(1 << N):
  #各アルファベットの個数をカウント
  cnt = [0] * 26
  #for 選んでいる文字列一個一個に対して
  for i in range(N):
    #i番目のbitが1かどうかをチェック
    if (mask >> i) & 1: #&1で一番右だけ取り出せる
      #一文字ずつチェックしてcntの配列に入れていく
      for ch in S[i]:
        index = ord(ch) - ord('a')
        cnt[index] += 1

  #その選び方でのcntが終わったら
  #ちょうどK回登場するアルファベットが何個あるかを数えて
  score = 0
  for x in cnt:
    if x == K:
      score += 1
  #暫定値より大きかったら更新
  ans = max(ans, score)

print(ans)
  
