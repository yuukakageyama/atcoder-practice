
N = int(input())
S = []
T = []
for _ in range(N):
  s, t = input().split()
  t = int(t)
  S.append(s)
  T.append(t)

score = -1
ans = 0
poem_set = set()
for i in range(N):
  if S[i] not in poem_set:
    #オリジナルだったら作品の集合に追加
    poem_set.add(S[i]) 
    
    if T[i] > score:
      ans = i+1
      score = T[i]

print(ans)

