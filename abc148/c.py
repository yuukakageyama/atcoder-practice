A, B = map(int, input().split())

if A < B:
  t = B
  B = A
  A = t

def gcd(a,b):
  while b!= 0:
    t = b
    b = a % b
    a = t
  return a

  

print(A*B // gcd(A, B))
