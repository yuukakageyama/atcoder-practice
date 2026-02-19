#集合への追加はかぶってないときを自動的に判定
N = int(input())

S = set()

for _ in range(N):
  s = input().strip()
  S.add(s)

print(len(S))
