Q = int(input())
A = []
for i in range(Q):
  A.append(int(input()))
  
def musicplayer(A, i, volume, play_flag):
  if A[i] ==1:
    volume += 1
  elif A[i] == 2:
    if volume >= 1:
      volume -= 1
  else:
    if play_flag:
      play_flag = False
    else:
      play_flag = True
  return volume, play_flag

volume = 0
play_flag = False

for k in range(len(A)):
  volume, play_flag = musicplayer(A, k, volume, play_flag)
  if volume>=3 and play_flag == True:
    print("Yes")
  else:
    print("No")
