import math
X = int(input())

for i in range(X, 100004):
  is_prime = True
  for j in range(2, math.isqrt(i)):
    if i % j == 0:
      is_prime = False
  if is_prime:
    print(i)
    exit()
