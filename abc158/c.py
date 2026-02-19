A, B = map(int, input().split())

ans = -1
for i in range(1, 2000):
  if (8*i) // 100 == A and (10*i) // 100 ==B:
    ans = i
    break

print(ans)
