#計算量探索のために，差分だけを更新していく

N, Q = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

#最初の合計を作る
ans = 0
for i in range(N):
  ans += min(A[i], B[i])

#クエリ処理
for _ in range(Q):
  c, X, V = input().split()
  X = int(X) - 1 #インデックスにしておく
  V = int(V)
  
  #更新前のmin
  old = min(A[X], B[X])
  
  #更新
  if c == 'A':
    A[X] = V
  elif c == 'B':
    B[X] = V
  
  #更新後のmin
  new = min(A[X], B[X])
  
  #差分だけ反映
  ans += new - old
  
  print(ans)
