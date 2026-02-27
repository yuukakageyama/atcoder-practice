
N, M = map(int, input().split())
S = []
for _ in range(M):
  row = list(map(int, input().split()))
  k = row[0]
  S.append(row[1:1+k])

p = list(map(int, input().split()))

ans = 0
#bit全探索
#電球一個ごとでforループまわして必要な結果を保存？
#0, 1のパターンN桁を試す
for mask in range(1<<N):#N桁のbitパターンをそれぞれ回す
  ok = True #bitパターンごと
  for i in range(M): #各電球
    for sw in S[i]: #各スイッチ
      cnt = 0
      #1の数を数える
      if (mask >> (sw - 1)) & 1: #sw番目のスイッチがONかどうか
        cnt += 1
      if cnt % 2 != p[i]:
        ok = False
        break
  if ok:
    ans += 1
print(ans)
