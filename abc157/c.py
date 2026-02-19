N, M = map(int, input().split())

ans = -1

conds = []
for _ in range(M):
  s, c = map(int, input().split())
  conds.append((s,c))

start = 0 if N == 1 else 10 **(N-1)
end = 10**N

#N桁の数を順に試す
for i in range(start, end):
  i = str(i)
  
  #各組合せの条件チェック
  for s, c in conds:
    c = str(c)
    if i[s-1] != c:
      break
  else:
    ans = int(i)
    break
print(ans)
