#入力処理部分
N = int(input())

log = set()

#Nが1になったらおわり
while N != 1:
  #過去にあったらNo
  if N in log:
    print("No")
    break
  
  #なければログに追加
  log.add(N)
  
  #ここから各桁の二乗和を計算
  sum_square = 0
  for i in str(N):
    sum_square += int(i)**2
  N = sum_square

else:
  print("Yes")
