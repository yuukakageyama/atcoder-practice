#行，列の扱い方を学ぶ(特に列)
#残す行や列は別でリストを作成
#列はflagを利用
#入力は最初に全読み込み

H, W = map(int, input().split())
A = [input().strip() for _ in range(H)]
#残す行
row_ok = []
for i in range(H):
  if '#' in A[i]:
    row_ok.append(i)

#残す列
col_ok = []
for j in range(W):
  has_black = False
  for i in range(H):
    if A[i][j] == '#':
      has_black = True
      break
  if has_black:
    col_ok.append(j)

#出力
for i in row_ok:
  line = ""
  for j in col_ok:
    line += A[i][j]
  print(line)
