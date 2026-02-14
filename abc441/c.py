
  
  
#入力処理
N, K, X = map(int, input().split())

A = list(map(int, input().split()))

A.sort()

#累積和のリストpref[]
pref = [0] * (N+1)
for i in range(N):
  pref[i+1] = pref[i] + A[i]

def range_sum(l, r):
  """A[l:r]の和"""
  return pref[r] - pref[l]
  
ans = -1
#m個について考えていく
for m in range(1, N+1):
  #飲んだm個に必ず含まれる日本酒の最小個数
  #m個飲む，N-m個は飲まない，日本酒が入っているK個から飲まないのを引くと出る
  #日本酒K個を飲まない側N-m個に最大限押し込む
  r = max(0, K - (N-m))
  
  #日本酒が含まれない場合がありえたら次のループへ
  if r == 0:
    continue
  
  #大きい方から選んでいって，
  #日本酒r個がその集合の中の小さい方に配置される最悪ケースを考える
  #大きい方から順に飲むとする
  start = N -m #飲む集合はA[start:N]
  #start:start+r番目にお酒が配置されたときのお酒の量
  worst = range_sum(start, start + r)
  
  if worst >= X:
    ans = m
    break
  
print(ans)
