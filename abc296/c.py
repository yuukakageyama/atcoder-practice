#set(ハッシュ)を学ぶ
#集合を利用

N,X = map(int, input().split())

A = list(map(int, input().split()))

S = set(A)

for a in A:
  if a+X in S:
    print("Yes")
    break
else:
  print("No")
