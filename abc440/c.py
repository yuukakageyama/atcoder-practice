import sys
input = sys.stdin.readline

def solve():
  T = int(input().strip())
  out = []
  
  #各テストケース
  for _ in range(T):
    N, W = map(int, input().split())
    C = list(map(int, input().split()))
    
    L = 2 * W #2Wで割る余りだからこの周期
    w = [0] * L
    
    #iは1..Nなので余りはi % (2W)
    #Pythonの%は0..L-1を返す
    for idx, cost in enumerate(C, start = 1) :#配列Cをインデックス1から
      w[idx % L]  += cost #w[r] = i %Lを満たすすべてのiのc_iの合計
      
    w2 = w + w
    
    #ここからスライディングウィンドウ
    #w2の0~Wを足して最初の区間和を作成
    cur = sum(w2[:W])
    best = cur
    
    #1周期分
    for start in range(1, L):
      #区間和の更新式
      cur += w2[start + W-1] - w2[start-1]
      #最小値を保存
      if cur < best:
        best = cur
    
    out.append(str(best))
    
  print("\n".join(out))

if __name__ == "__main__":
  solve()
