#連続文字の圧縮(RLE : Run Length Encoding)
#ランレングス圧縮の関数を作る
#塊の数が同じ，並び方が同じ，回数に矛盾がない，という条件をさらう

def rle(s):
  res =[]
  i = 0 #iが今チェック中の文字
  n = len(s)
  while i < n: #まだ文字があれば
    j = i #ポインタj
    
    #チェック中の文字と同じ間はポインタjを進めていく
    while j < n and s[j] == s[i]:
      j += 1
    #(a,3)みたいなかんじ(今の文字, 連続回数)
    res.append((s[i], j-i))
    i = j
  return res

S = input().strip()
T = input().strip()

a = rle(S)
b = rle(T)

#塊の数が同じかどうか
if len(a) != len(b):
  print("No")

else:
  ok = True
  #塊の文字が同じ順に並んでいるかどうか
  for (ch1, c1), (ch2, c2) in zip(a,b):
    if ch1!= ch2:
      ok = False
      break
    
    #各塊について1だったら増やせないからtも1じゃないとだめ
    if c1 == 1:
      if c2 != 1:
        ok = False
        break
    else: #2個以上の場合はtの方が多ければよい
      if c2<c1:
        ok = False
        break
  print("Yes" if ok else "No")
