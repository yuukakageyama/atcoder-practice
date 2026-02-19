H, W = map(int, input().split())

S = [input().strip() for _ in range(H)]

row_has = [False] * H #行
col_has = [False] * W #列

#どの行・列に#があるか記録
for i in range(H):
  for j in range(W):
    if S[i][j] == '#':
      row_has[i] = True
      col_has[j] = True

# #がある行の最小・最大
top = None
bottom = None
for i in range(H):
  if row_has[i]:
    if top is None:
      top = i
    bottom = i

# #がある列の最小・最大
left = None
right = None
for j in range(W):
  if col_has[j]:
    if left is None:
      left = j
    right = j
    
# 外接矩形の中で.を探す
for i in range(top, bottom+1):
  for j in range(left, right+1):
    if S[i][j] == '.':
      print(i+1, j+1)
      exit()
