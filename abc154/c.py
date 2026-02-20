
N = int(input())
A = set(map(int, input().split()))

if len(A) == N:
  print("YES")
elif len(A) < N:
  print("NO")

