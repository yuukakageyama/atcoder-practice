#累積和を学ぶ

N, Q = map(int, input().split())
S = input().strip()

#pref[i] は S[0:i]の中にACが何回あるか
pref = [0] * (N+1)

for i in range(N-1):
  pref[i+1] = pref[i]
  if S[i] == 'A' and S[i+1] == 'C':
    pref[i+1] += 1

pref[N] = pref[N-1]

for _ in range(Q):
  l, r = map(int, input().split())
  print(pref[r-1] - pref[l-1])

