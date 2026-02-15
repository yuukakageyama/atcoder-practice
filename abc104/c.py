#bit演算を学ぶ
#今回はコンプリートするを1, しないを0として設定
#mask & (1<<i)でその桁が1かどうかチェックできる

D, G = map(int, input().split())

p = []
c = []
for _ in range(D):
  pi, ci= map(int, input().split())
  p.append(pi)
  c.append(ci)

ans = 10 **18

#0~2^D-1の全パターン
for mask in range(1 << D): #1をDbit左へシフト
  score = 0
  cnt = 0
  
  # 1) maskでコンプリートするグループを全部足す
  for i in range(D):
    #maskのi番目のビットが1かどうかをチェックしている
    #001, 010, 100などiビットだけ1をシフトしたものとmaskを論理和
    if mask & (1 << i):
      score += 100 * (i+1) * p[i] + c[i]
      #cntは解いた問題数
      cnt += p[i]
      
  # 2) それで目的の点数に達していたらら最小更新
  if score >= G:
    ans = min(ans, cnt)
    continue #次のmaskに
  
  #3) 足りないなら，未コンプリートの中で高得点から追加で解く
  need = G - score #あと何点必要か
  tmp_cnt = cnt #ここで累積用を作る
  #D-1から0まで1ずつ減らしていく, 配点ごとにチェックしていく
  for i in range(D-1, -1, -1):
    if mask &(1 << i):
      continue #もうコンプリート済みのグループは追加しない
    
    val = 100 *(i+1) #このグループの1問あたり点
    
    #何問必要か(need÷valを切り上げする式)
    k = (need + val - 1) // val
    
    #ただし全部解くとボーナスが絡むので，ここでは最大p[i] -1まで
    k = min(k, p[i] -1)
    
    need -= k*val
    tmp_cnt += k #3)の操作のiのforループ後問題数
    
    if need <= 0:
      ans = min(ans, tmp_cnt)
      break
  
print(ans)
  
  
