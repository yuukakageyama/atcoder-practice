#二分探索
A, B, X = map(int, input().split())

def cost(n):
  return A*n + B*len(str(n))

ok = 0
ng = 10**9+1 #買えない側

while ng - ok > 1:
  middle  = (ok + ng) // 2
  if cost(middle) <= X:
    ok = middle
  else:
    ng = middle

print(ok)
    
