#入出力のstripの使い方
#集合setの使い方
#forループの配列のときの for word in w:みたいな使い方

#入力処理部分
N, M = map(int, input().split())
S = input().strip()
T = input().strip()
Q = int(input())

w = []
for _ in range(Q):
  w.append(input().strip())

#集合setを作る
setS = set(S)
setT = set(T)

for word in w:
  okS = True
  okT = True
  
  for c in word:
    if c not in setS:
      okS = False
    if c not in setT:
      okT = False
  if okS and okT:
    print("Unknown")
  elif okS:
    print("Takahashi")
  else:
    print("Aoki")
