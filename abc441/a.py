P, Q= map(int, input().split())
X, Y = map(int, input().split())

right_P = P+100
under_Q = Q+100

if P <= X < right_P and Q <= Y < under_Q:
  print("Yes")
else:
  print("No")
