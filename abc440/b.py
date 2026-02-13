#入力処理部分
N = int(input())

T = list(map(int, input().split()))

#ペアを作る
pairs = []

#馬のタイム, 馬番号
for i in range(N):
  pairs.append((T[i], i+1))

#sortは第一引数を優先，同じだったら第二引数で比較
pairs.sort()

print(pairs[0][1], pairs[1][1],pairs[2][1])
