N, S, K = map(int, input().split())
ans = 0

for i in range(N):
    p, q = map(int, input().split())
    ans += (p*q)

if ans < S:
    ans+=K

print(ans)