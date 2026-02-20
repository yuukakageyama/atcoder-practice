import math
X = int(input())

for i in range(X, 100004):
  if i < 2:
    continue  
  is_prime = True
  for j in range(2, math.isqrt(i) + 1):
    if i % j == 0:
      is_prime = False
      break
  if is_prime:
    print(i)
    exit()
