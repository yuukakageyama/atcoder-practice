#bit演算を学ぶ
#今回はコンプリートするを1, しないを0として設定
#mask & (1<<i)でその桁が1かどうかチェックできる

X, N = map(int, input().split())

p = set()
#1行のときはforループじゃなくてlistとかset
if N > 0:
  p = set(map(int, input().split()))

for d in range(150):
  if (X-d) not in p:
    print(X-d)
    break
  if(X+d) not in p:
    print(X+d)
    break
