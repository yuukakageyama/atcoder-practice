#グラフ問題の処理，今回は次数だけに注目して解いた

#入力の処理がより速いreadlineにしてるらしい
import sys
input = sys.stdin.readline
#入力処理部分
N, M = map(int, input().split())
#その研究者が何人と利害関係をもつか記録する次数(degree)のリスト
deg = [0] * (N+1)

#A, Bの配列自体は持たなくてよい．
#degreeだけ計算していけばよい
#利害関係で何回出てきたかを記録
for _ in range(M):
  a, b = map(int, input().split())
  deg[a] += 1
  deg[b] += 1

#combinationの３個選ぶやつを関数化  
def comb3(x: int) -> int:
  return x* (x-1) * (x-2) // 6 if x >= 3 else 0

res = []
for i in range(1, N + 1):
  x = (N-1) - deg[i]
  res.append(str(comb3(x)))

#joinは""の中を入れたうえでつなげる
#今回はspace区切りで配列をつなげてprint
print(" ".join(res))
