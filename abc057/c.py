N = int(input())

import math
ans = 10**18

#Nの整数平方根(平方根の切り下げ)
for a in range(1, int(math.isqrt(N)) + 1):
  if N % a == 0:
    b = N // a
    f = max(len(str(a)), len(str(b)))
    if f < ans:
      ans = f

print(ans)
