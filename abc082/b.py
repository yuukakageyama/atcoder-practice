#Pythonは文字列同士を辞書順比較できる

s = input().strip()
t = input().strip()

#sを昇順
#tを降順にして比較
s_min = ''.join(sorted(s))
t_max = ''.join(sorted(t, reverse=True))

if s_min < t_max:
  print("Yes")
else:
  print("No")
