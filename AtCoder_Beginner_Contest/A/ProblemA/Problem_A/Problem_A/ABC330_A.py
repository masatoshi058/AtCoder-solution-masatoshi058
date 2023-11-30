n, l = map(int, input().split())
lis = map(int, input().split())

a = list(lis)

count = 0
for score in a:
    if score >= l:
      count += 1

print(count)

# N, L = map(int, input().split())
# A = list(map(int, input().split()))

# ans = 0
# for a in A:
#     if a >= L:
#         ans += 1
# print(ans)