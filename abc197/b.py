
H, W, X, Y = map(int, input().split())
cnt = 1
S = []
for _ in range(H):
  S.append(input().strip())

X -= 1
Y -= 1


#上が.だったら1追加#きたらおわり
for i in range(X-1, -1, -1):
  if S[i][Y] == '.':
    cnt += 1
  else:
    break

for j in range(X+1, H):
  if S[j][Y] == '.':
    cnt += 1
  else:
    break

for k in range(Y-1, -1, -1):
  if S[X][k] == '.':
    cnt += 1
  else:
    break

for l in range(Y+1, W):
  if S[X][l] == '.':
    cnt += 1
  else:
    break

print(cnt)
